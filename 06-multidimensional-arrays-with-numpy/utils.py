import os
import numpy as np
import pickle
from sklearn.datasets import load_breast_cancer

def load_heights():
    with open('heights.txt', 'r') as f:
        a = np.array([list(map(float, line.strip().split())) for line in f.readlines()[1:]])
    
    return a


def load_heights2():
    with open('heights2d.pkl', 'rb') as f:
        return pickle.load(f)
    
    
def load_cancer():
    dataset = load_breast_cancer()
    values = dataset.data
    columns = dataset.feature_names
    target = dataset.target
    return columns, values, target