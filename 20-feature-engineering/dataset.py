import numpy as np
import os
import pandas as pd


def load_california_housing_prices():
    train_dataset = pd.read_csv(
        os.path.join("data", "california_housing_train.csv"), 
        index_col=0
    )
    test_dataset = pd.read_csv(
        os.path.join("data", "california_housing_test.csv"), 
        index_col=0
    )
    return {
        "train": {
            "x": train_dataset.drop(["median_house_value"], axis=1),
            "y": train_dataset[["median_house_value"]]
        },
        "test": {
            "x": test_dataset.drop(["median_house_value"], axis=1),
            "y": test_dataset[["median_house_value"]]
        }
    }
