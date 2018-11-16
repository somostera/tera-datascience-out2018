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
        self.imputer = Imputer(strategy="median")
        self.columns = columns
        
    def fit(self, X, y=None, **fit_params):
        self.imputer.fit(X.loc[:, self.columns])
        return self
    
    def transform(self, X):
        X_t = X.copy()
        X_t.loc[:, self.columns] = self.imputer.transform(X_t.loc[:, self.columns])
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
        X_t = X[self.columns].apply(np.log).rename(columns=lambda c: f"log_of_{c}")
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
        self.imputer = LogisticRegression(
            max_iter=1000,
            solver="newton-cg", 
            multi_class="multinomial"
        )
        
    def fit(self, X, y=None, **fit_params):
        target_feat = "ocean_proximity"
        inputs_cols = ["latitude", "longitude"]
        
        index = X[target_feat].isin(self.valid_categories)
        
        x_train = X.loc[index, inputs_cols]
        y_train = X.loc[index, target_feat]
        
        self.imputer.fit(x_train, y_train)
        return self
    
    def transform(self, X):
        target_feat = "ocean_proximity"
        inputs_cols = ["latitude", "longitude"]
        
        X_t = X.copy()
        index = X_t[target_feat].isnull()
        X_t.loc[index, target_feat] = self.imputer.predict(X_t.loc[index, inputs_cols])
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
        
        dummy = pd.get_dummies(
            X["ocean_proximity"], 
            prefix="ocean_proximity",
            prefix_sep=": "
        ) 
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
        
        # Início das transformações manuais; 
        # repita as linhas abaixo para cada transformação
        
        X_t.loc[:, "bedrooms per rooms"] = X_t.total_bedrooms / X_t.total_rooms
        X_t.loc[:, "bedrooms per house"] = X_t.total_bedrooms / X_t.households
        X_t.loc[:, "rooms per house"] = X_t.total_rooms / X_t.households
        X_t.loc[:, "people per house"] = X_t.population / X_t.households
        
        # Fim das transformações
        
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
        
        x_poli = pd.DataFrame(
            index=X.index,
            columns=self.polifeat.get_feature_names(self.features),
            data=self.polifeat.transform(X[self.features])
            
        )
        
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
            distance_lat = (X_t.latitude - self.poi[k][0]) ** 2
            distance_lon = (X_t.longitude - self.poi[k][1]) ** 2
            x_poi.loc[:, f"Distance to {k}"] = (distance_lat + distance_lon) ** 0.5
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
