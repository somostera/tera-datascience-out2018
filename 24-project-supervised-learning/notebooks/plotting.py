import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc


def multiple_histograms_plot(data, x, hue, bins=10,
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
        data.loc[current_hue_mask, x].hist(bins=bins, alpha=alpha, 
                                           label=str(current_hue), 
                                           color=colors_dict[current_hue]) 
    
    xlabel = x if xlabel is None else xlabel
    ylabel = (ylabel if ylabel is not None 
                     else 'Frequency')
    
    title = f'{xlabel} by {hue}'
    
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

        
def bar_plot_with_categorical(df, x, hue, order=None, figsize=(16, 8),
                              plot_average=True, xticklabels=None, 
                              **sns_kwargs):
    if order is None:
        order = (pd.pivot_table(data=df, values=hue, index=[x], aggfunc='mean')
                   .sort_values(by=hue, ascending=False)
                   .index.values)
    
    plt.subplots(figsize=figsize)
    sns.barplot(x=x, y=hue, data=df, order=order, **sns_kwargs)
    
    if plot_average:
        hue_average = df[hue].mean()
        plt.axhline(y=hue_average, linewidth=2, linestyle='--', 
                    color='gray', label='{} average'.format(hue))
    
    if xticklabels is not None:
        ax = plt.gca()
        ax.set_xticklabels(xticklabels)
        
    plt.legend()
    plt.show()


def plot_confusion_matrix(y_true, y_pred,
                          index_labels=('False (truth)', 'True (truth)'),
                          columns_labels=('False (pred)', 'True (pred)')):
    
    conf_matrix = confusion_matrix(y_true, y_pred)
    conf_matrix_df = pd.DataFrame(conf_matrix, index=index_labels,
                                  columns=columns_labels)
    _, ax = plt.subplots(figsize=(8, 8))
    ax.set_title('Confusion Matrix')
    sns.heatmap(conf_matrix_df, annot=True, fmt="d", linewidths=10,
                cmap='Blues', ax=ax)


def plot_roc(y_true, y_score, figsize=(8, 8)):
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, color='darkorange',
             lw=2, label=f'ROC curve (AUC = {100*roc_auc:.2f}%)')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()
    
    return roc_auc
