import pandas as pd
from tqdm import tqdm
from lightgbm import LGBMModel
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import get_scorer

from evaluation import grid_search_report


def find_n_estimators(model: LGBMModel, X_train, y_train, eval_metric,
                      learning_rates=[0.01, 0.03, 0.1, 0.3],
                      max_depths=range(1, 6),
                      max_n_estimators=20000, early_stopping_rounds=200,
                      validation_size=0.25, random_state=None, verbose=True):
    """Optimizes the 'n_estimators' parameters using the early stopping method.
    
    For each tuple containing 'learning_rate' and 'max_depth',
    it optimizes 'n_estimators' using the early stopping technique which is implemented by LightGBM.
    """
    X_dev, X_val, y_dev, y_val = train_test_split(X_train, y_train, 
                                                  test_size=validation_size, 
                                                  random_state=random_state)

    results = pd.DataFrame(columns=['learning_rate', 'max_depth',
                                    'best_score', 'best_n_estimators'])
    
    for learning_rate in tqdm(learning_rates, desc='learning rates', disable= not verbose):
        for max_depth in tqdm(max_depths, desc='max depths', disable=not verbose):
            
            model.learning_rate = learning_rate
            model.max_depth = max_depth
            model.n_estimators = max_n_estimators
            model.random_state = random_state

            model.fit(X_dev, y_dev, eval_set=(X_val, y_val), eval_metric=eval_metric,
                      early_stopping_rounds=early_stopping_rounds, verbose=False)
                    
            results = results.append({'learning_rate': learning_rate, 
                                      'max_depth': max_depth,
                                      'best_score': model.best_score_['valid_0'][eval_metric],
                                      'best_n_estimators': model.best_iteration_}, 
                                     ignore_index=True)
    
    results['max_depth'] = results['max_depth'].astype(int)
    results['best_n_estimators'] = results['best_n_estimators'].astype(int)

    return results


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
