import pandas as pd
    
    
# ---------------------------------- #
#                                    #
#           Tarefa (1.3)             #
#                                    #
# ---------------------------------- #

        
def calculate_outliers(X):
    """ Função auxiliar que calcula os elementos da base de treino que devem 
        ser eliminados usando cortes pré-definidos. 
    """
    # exercício - INI
    # defina os cortes a serem aplicados na massa de treino
    cuts_list = [
        # (feat, lim_inf, lim_sup),
        ("log_of_total_rooms", 5, 10),
        ("log_of_total_bedrooms", 4, 8),
        ("log_of_population", 5, 9),
        ("log_of_households", 4, 8),
        ("log_of_median_income", -.5, 2.7)
    ]
    # exercício - FIM
    
    cuts_table = pd.DataFrame(columns=["count", "percent"])
    keep_index = pd.Series(index=X.index, data=True)
    for feat, lim_inf, lim_sup in cuts_list:
        cuts_index = (X[feat] < lim_inf) | ((X[feat] > lim_sup))
        cuts_table = cuts_table.append(
            pd.DataFrame(
                index=[f"{lim_inf} <= {feat} <= {lim_sup}"],
                columns=["count", "percent"],
                data=[[cuts_index.sum(), cuts_index.mean()]]
            )
        )
        keep_index &= ~cuts_index
    cuts_table = cuts_table.append(
        pd.DataFrame(
            index=[f"Total Elements Cut"],
            columns=["count", "percent"],
            data=[[(~keep_index).sum(), (~keep_index).mean()]]
        )
    )
    return keep_index, cuts_table
