import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import requests
import re
from unidecode import unidecode
import yaml
import io
from pathlib import Path
import time
import math
from math import sqrt
import json

# ------------
# data pre-processing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    LabelEncoder
    ,OrdinalEncoder
    ,OneHotEncoder
)
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
# ------------
# model
from sklearn.linear_model import (
    Ridge
    ,LinearRegression
    ,Lasso
        ,SGDRegressor
)
from sklearn.model_selection import (
    GroupKFold,
    GroupShuffleSplit,
    KFold,
    ShuffleSplit,
    StratifiedGroupKFold,
    StratifiedKFold,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# ------------
# metric
from sklearn.metrics import (
    mean_squared_error
    ,r2_score
    ,mean_absolute_error
)

from matplotlib.colors import LinearSegmentedColormap


def show_null_values(df):
    df_no_null_values = df.isna().sum().rename('Num of null rows')
    df_pct_null_values = (df.isna().sum() * 100/ len(df)).round(4).rename('PCT of null rows')

    result = pd.concat(
        [df_no_null_values, df_pct_null_values]
        , axis=1
    )

    return result


def show_distribution_of_attributes(df, bins=40, figsize=(12,8)):
    df.hist(bins=bins, figsize=figsize)
    plt.show()

def show_correlation_heatmap(df, option:int=1):
    """
    option=1: hide the diagonal of 1s
    option=2: hide the diagonal of 1s and the upper triangle
    """
    corr_info = df.corr()
    if option == 1:
        mask = np.eye(len(corr_info), dtype=bool)
    elif option == 2:
        mask = np.triu(np.ones_like(corr_info, dtype=bool))

        
    sns.heatmap(
        corr_info
        ,annot=True
        ,mask=mask
        ,fmt=".2f"
        ,cmap='coolwarm'
    )
    plt.show()

def show_vif(df):
    X_vif = df.copy()
    imputer = SimpleImputer(strategy='median')
    X_vif_imputed = pd.DataFrame(imputer.fit_transform(X_vif), columns=X_vif.columns)


    from statsmodels.tools.tools import add_constant
    X_vif_final = add_constant(X_vif_imputed)

    vif_data = pd.DataFrame()
    vif_data['feature'] = X_vif_final.columns
    vif_data['VIF'] = [variance_inflation_factor(X_vif_final.values, i) for i in range(len(X_vif_final.columns))]
    vif_data = vif_data[vif_data['feature'] != 'const']
    return vif_data.sort_values(by='VIF', ascending=False)
