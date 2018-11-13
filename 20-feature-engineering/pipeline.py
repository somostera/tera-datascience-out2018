import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Imputer, PolynomialFeatures


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                       PARTE 1                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# ---------------------------------- #
#                                    #
#           Tarefa (1.1)             #
#                                    #
# ---------------------------------- #

class NumericalFeaturesImputer(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer baseada em um Imputer de Mediana.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self, columns):
        # exercício - INI  
        # >> Crie o Imputer com a configuração correta
        self.imputer = None
        # exercício - FIM
        self.columns = columns
        
    def fit(self, X, y=None, **fit_params):
        # exercício - INI        
        ## >> treine o Imputer apenas com as features desejadas
        # exercício - FIM
        return self
    
    def transform(self, X):
        X_t = X.copy()
        # exercício - INI        
        ## >> Atualize os valores nulos de X_t, apenas nas features desejadas, usando o Imputer
        # exercício - FIM
        return X_t

    
# ---------------------------------- #
#                                    #
#           Tarefa (1.2)             #
#                                    #
# ---------------------------------- #

class LogFeaturesTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer para aplicar log em valores numéricos.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self, columns):
        self.columns = columns
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X):
        X_t = X.copy()        
        # exercício - INI        
        ## >> Aplique a função correta nos valores de X_t, apenas nas features desejadas
        ## >> Renomeie as colunasde X_t, apenas nas features desejadas, para o padrão mostrado no notebook
        # exercício - FIM
        return X.join(X_t)

    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                       PARTE 2                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# ---------------------------------- #
#                                    #
#           Tarefa (2.1)             #
#                                    #
# ---------------------------------- #

class CategoricalFeaturesImputer(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer baseada em um Imputer Categórico que busca a categoria 
        do elemento mais próximo.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self, valid_categories):
        self.valid_categories = valid_categories
        # exercício - INI  
        # >> Crie o Imputer com a configuração correta
        self.imputer = None
        # exercício - FIM
        
    def fit(self, X, y=None, **fit_params):
        target_feat = "ocean_proximity"          # valor a ser estimado
        inputs_cols = ["latitude", "longitude"]  # features a serem utilizadas
        # exercício - INI        
        ## >> treine o Imputer 
        # exercício - FIM
        return self
    
    def transform(self, X):
        target_feat = "ocean_proximity"          # valor a ser estimado
        inputs_cols = ["latitude", "longitude"]  # features a serem utilizadas
        X_t = X.copy()
        # exercício - INI        
        ## >> estime o valor desejado apenas onde ele é nulo 
        # exercício - FIM
        return X_t

    
# ---------------------------------- #
#                                    #
#           Tarefa (2.2)             #
#                                    #
# ---------------------------------- #

class CategoricalToDummyFeaturesTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer que transforma labels na representação Dummy.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self, categories):
        self.categories = [f"ocean_proximity: {c}" for c in categories]
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X):        
        X_t = X.drop("ocean_proximity", axis=1)
        categories = X["ocean_proximity"]
        
        # exercício - INI        
        ## >> transforme `categories` em dummies (formato de DataFrame)
        ##    e armazene a resposta na variável `dummy` 
        dummy = None
        # exercício - FIM
        
        return X_t.join(dummy.loc[:, self.categories])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                       PARTE 3                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# ---------------------------------- #
#                                    #
#           Tarefa (3.1)             #
#                                    #
# ---------------------------------- #

class ManuallyCraftedFeaturesTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer que aplica transformações manuais.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """    
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X):        
        X_t = X.copy()
        
        # exercício - INI        
        # >> repita a linha abaixo para cada transformação
        #  ... 
        #     X_t.loc[:, "nome da nova feature"] = <combinação de features>
        #  ...
        # exercício - FIM        
        
        return X_t


# ---------------------------------- #
#                                    #
#           Tarefa (3.2)             #
#                                    #
# ---------------------------------- #

class PolynomialFeaturesTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer que cria features não lineares usando Transformação Polinomial.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self, features, degree):
        self.features = features
        self.polifeat = PolynomialFeatures(degree=degree, include_bias=False)
        
    def fit(self, X, y=None, **fit_params):
        self.polifeat.fit(X[self.features])
        return self
    
    def transform(self, X):        
        X_t = X.drop(self.features, axis=1)        
        X_t = X.copy()
        
        # exercício - INI        
        # >> Use a função de transformação corretamente e armazene o resultado em `x_poli`
        # >> Gere nomes descritivos para as features geradas (nas colunas)
        x_poli = None
        # exercício - FIM        
        
        return X_t.join(x_poli)


# ---------------------------------- #
#                                    #
#           Tarefa (3.3)             #
#                                    #
# ---------------------------------- #

class PointsOfInterestFeaturesTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer que cria features baseadas na distância a pontos de interesse.
        Esse imputer mantém a entrada X como um DataFrame em vez de transformar em numpy.array.
    """
    
    def __init__(self):
        self.poi = {
            "Malibu": (34.0334867, -118.8798692),
            "Disneyland": (33.8120962, -117.9211629),
            "Golden Gate": (37.8199328, -122.4804438),
            "Oakland": (37.7586639, -122.3754148),
            "San Diego": (32.8407296,-117.3980308),
        }
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X):        
        X_t = X.copy()        
        x_poi = pd.DataFrame(index=X_t.index)        
        for k in self.poi:
            # exercício - INI        
            # >> para cada local de interesse, calcule a distância à lat/lon do elemento
            x_poi.loc[:, f"Distance to {k}"] = None
            # exercício - FIM    
        return X_t.join(x_poi)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                       Auxiliares                                                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class FeaturesChoiceTransform(BaseEstimator, TransformerMixin):
    """ Classe de Feature Transformer que filtra as colunass referentes às features de interesse.
    """
    
    def __init__(self, columns):
        self.columns = columns
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X):
        X_t = X.copy()
        return X_t.loc[:, self.columns]
