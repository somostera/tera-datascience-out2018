import numpy as np
import pandas as pd

from sklearn.metrics import classification_report, get_scorer
from plotting import multiple_histograms_plot, plot_confusion_matrix


def predictions_hist(y_pred_proba, y_test, density=True):
    preds_df = pd.DataFrame(data=[y_pred_proba, y_test.astype(str)],
                            index=['Prediction', 'True Value']).T

    preds_df['Prediction'] = preds_df['Prediction'].astype(float)
    preds_df['True Value'] = preds_df['True Value'].astype(str)

    multiple_histograms_plot(data=preds_df, x='Prediction', hue='True Value',
                             bins=np.arange(0, 1.1, 0.025), density=density, probability_hist=True)

    return preds_df


def confusion_matrix_report(y_test, y_pred_proba, thres=0.5):
    y_pred_proba_customizado = y_pred_proba >= thres
    print(classification_report(y_test, y_pred_proba_customizado))
    plot_confusion_matrix(y_test, y_pred_proba_customizado)

    
def _grid_search_report(grid_scores, scoring, round_ndigits=6):
    mean_scoring = 'mean_median_percentage_error'
    grid_scores_df = pd.DataFrame(columns=[mean_scoring, 'std', 
                                           'n_estimators', 'learning_rate', 
                                           'max_depth'])
    
    for idx, scores in enumerate(grid_scores):
        grid_scores_df.loc[idx, mean_scoring] = -scores[1]
        grid_scores_df.loc[idx, 'std'] = scores[2].std()
        grid_scores_df.loc[idx, 'n_estimators'] = scores[0]['n_estimators']
        grid_scores_df.loc[idx, 'learning_rate'] = scores[0]['learning_rate']
        grid_scores_df.loc[idx, 'max_depth'] = scores[0]['max_depth']

    return (grid_scores_df
                .applymap(lambda x: round(x, round_ndigits))
                .sort_values(by=[mean_scoring, 'std', 'n_estimators'], 
                             ascending=True))


def grid_search_report(grid_scores, scoring, scoring_alias=None, round_ndigits=6, include_learning_rate=False):
    mean_scoring = f'mean_{scoring_alias}' if scoring_alias is not None else f'mean_{scoring}'
    
    grid_scores_cols = [mean_scoring, 'std', 'n_estimators', 'learning_rate', 'max_depth']
    if not include_learning_rate:
        grid_scores_cols.remove('learning_rate')
    
    grid_scores_df = pd.DataFrame(columns=grid_scores_cols)
    
    scoring_sign = scoring._sign if not isinstance(scoring, str) else get_scorer(scoring)._sign
    
    for idx, scores in enumerate(grid_scores):
        grid_scores_df.loc[idx, mean_scoring] = scoring_sign * scores[1]
        grid_scores_df.loc[idx, 'std'] = scores[2].std()
        grid_scores_df.loc[idx, 'n_estimators'] = scores[0]['n_estimators']
        grid_scores_df.loc[idx, 'max_depth'] = scores[0]['max_depth']
        if include_learning_rate:
            grid_scores_df.loc[idx, 'learning_rate'] = scores[0]['learning_rate']

    return (grid_scores_df
                .applymap(lambda x: round(x, round_ndigits))
                .sort_values(by=['std', 'n_estimators'], ascending=True)
                .sort_values(by=mean_scoring, ascending=(scoring_sign < 0)))