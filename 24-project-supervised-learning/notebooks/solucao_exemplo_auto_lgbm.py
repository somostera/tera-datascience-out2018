import pandas as pd
from tqdm import tqdm
from lightgbm import LGBMModel
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import get_scorer

from solucao_exemplo_evaluation import grid_search_report


def find_n_estimators(model: LGBMModel, X_train, y_train, eval_metric,
                      learning_rates=[0.01, 0.03, 0.1, 0.3],
                      max_n_estimators=20000, early_stopping_rounds=200,
                      validation_size=0.25, random_state=None, verbose=True):
    """Optimizes the 'n_estimators' parameters using the early stopping method.
    
    For each tuple containing 'learning_rate' and 'max_depth',
    it optimizes 'n_estimators' using the early stopping technique which is implemented by LightGBM.
    """
    X_dev, X_val, y_dev, y_val = train_test_split(X_train, y_train, 
                                                  test_size=validation_size, 
                                                  random_state=random_state)

    results = pd.DataFrame(columns=['learning_rate', 'best_score', 
                                    'best_n_estimators'])
    
    for learning_rate in tqdm(learning_rates, desc='learning rates', disable= not verbose):
            
        model.learning_rate = learning_rate
        model.n_estimators = max_n_estimators
        model.random_state = random_state

        model.fit(X_dev, y_dev, eval_set=(X_val, y_val), eval_metric=eval_metric,
                  early_stopping_rounds=early_stopping_rounds, verbose=False)
                
        results = results.append({'learning_rate': learning_rate, 
                                  'best_score': model.best_score_['valid_0'][eval_metric],
                                  'best_n_estimators': model.best_iteration_}, 
                                 ignore_index=True)
    
    results['best_n_estimators'] = results['best_n_estimators'].astype(int)

    return results


def make_param_grids(n_estimators_result: pd.DataFrame, best_score_col='best_score', top=3):
    """ Creates a list of param grids to be used in a grid search.
    """
    param_grids = (n_estimators_result.sort_values(by=best_score_col).head(top)
                       .drop(columns=best_score_col)
                       .rename(columns={'best_n_estimators': 'n_estimators'})
                       .sort_values(by=['learning_rate'])
                       .to_dict('records'))
    
    for grid in param_grids:
        for param_name, value in grid.items():
            if param_name == 'n_estimators':
                grid[param_name] = [int(value)]
            else:
                grid[param_name] = [value]
    
    return param_grids


def grid_search(model: LGBMModel, X_train, y_train, param_grids, 
                scoring, scoring_alias=None, cv=3, verbose=2):
    """ Grid Search with LightGBM-specific reporting output.
    """
    grid_search_cv = GridSearchCV(model, param_grids, scoring=scoring, 
                                  cv=cv, verbose=verbose)
    
    grid_search_cv.fit(X_train, y_train, verbose=False)
    
    report = grid_search_report(grid_search_cv.grid_scores_, scoring, 
                                scoring_alias=scoring_alias,
                                include_learning_rate=True)
    
    return (report, grid_search_cv.best_estimator_)
