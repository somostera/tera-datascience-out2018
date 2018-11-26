import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_recall_curve
import itertools


def multiple_histograms_plot(data, x, hue, density=False, bins=10,
                             alpha=0.5, colors=None, hue_order=None,
                             probability_hist=False, xticks=None, 
                             title=None, xlabel=None, ylabel=None, 
                             figsize=(15, 8), xticklabels=None):
    
    hue_order = hue_order if hue_order is not None else sorted(data[hue].unique())
    colors = colors if colors is not None else sns.color_palette(n_colors=len(hue_order))
    colors_dict = dict(zip(hue_order, colors)) 
    
    plt.figure(figsize=figsize)
    for current_hue in hue_order:
        current_hue_mask = data[hue] == current_hue
        data.loc[current_hue_mask, x].hist(bins=bins, density=density,
                                           alpha=alpha, label=str(current_hue), 
                                           color=colors_dict[current_hue]) 
    
    xlabel = x if xlabel is None else xlabel
    ylabel = (ylabel if ylabel is not None 
                     else 'Density' if density 
                     else 'Frequency')
    
    _title_postfix = ' (normalized)' if density else ''
    title = f'{xlabel} by {hue}{_title_postfix}'
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    
    ax = plt.gca()
    if probability_hist:
        plt.xlim(-0.0001, 1.0001)
        ax.set_xticks(np.arange(0, 1.1, 0.1))
        ax.set_xticks(np.arange(0.05, 1, 0.1), minor=True)
    elif xticks is not None:
        ax.set_xticks(xticks)
    
    if xticklabels is not None:
        ax.set_xticklabels(xticklabels)
        

def countplot_independent_ylims(df, col, hue, size=5, hue_order=None, title=None):
    g = sns.FacetGrid(df, col=hue, sharey=False, size=size)
    g = g.map(sns.countplot, col, order=hue_order)
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle(title)


def plot_1d_corr_heatmap(corr: pd.Series, annot=True, fmt='.2f', 
                         cmap='coolwarm'):
    max_corr = corr.abs().max()
    heatmap_df = pd.DataFrame(corr.sort_values(ascending=False))
    plt.subplots(figsize=(1.5, len(corr)//3.5))

    sns.heatmap(heatmap_df, annot=annot, fmt=fmt, cmap=cmap,
                center=0, vmin=-max_corr, vmax=max_corr)


# adapted from http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
def plot_confusion_matrix(y_test, y_pred, 
                          class_names,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    """
    cm = confusion_matrix(y_test, y_pred)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def precision_recall(y_test, y_score) -> pd.DataFrame:
    """Imprime a curva precision-recall e retorna os dados.
    
    Parâmetros:
        - y_test: os valores verdadeiros.
        - y_score: os scores calculados pelo modelo.
    
    Retorno:
        - um DataFrame contendo precisão, recall e f1-score para cada 
        threshold calculado.
    """
    precision, recall, thresholds = _precision_recall_plot(y_test, y_score)
    return _precision_recall_results(precision, recall, thresholds)


# adapted from http://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
def _precision_recall_plot(y_test, y_score):
    precision, recall, thresholds = precision_recall_curve(y_test, y_score)

    plt.step(recall, precision, color='b', alpha=0.2,
             where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2,
                     color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall curve')
    
    return precision, recall, thresholds


def _precision_recall_results(precision, recall, thresholds):
    results = pd.DataFrame(data=[precision, recall, thresholds],
                           index=['precision', 'recall', 'threshold']).T

    results['f1_score'] = (2 * (results['precision'] * results['recall']) 
                             / (results['precision'] + results['recall']))
    
    return results
