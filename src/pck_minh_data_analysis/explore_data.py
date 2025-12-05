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

def show_null_values(df):
    df_no_null_values = df.isna().sum().rename('Num of null rows')
    df_pct_null_values = (df.isna().sum() * 100/ len(df)).round(4).rename('PCT of null rows')

    result = pd.concat(
        [df_no_null_values, df_pct_null_values]
        , axis=1
    )

    return result

def normalize_column_name(df):
    result = []
    for col in df.columns:
        col = re.sub('(\n|\t)', '', col) # replace \n and \t with ''
        col = col.lower() # lower
        col = re.sub(' ', '_', col) # repace ' ' with '_'
        col = unidecode(col) # remove accent
        result.append(col)
    df.columns = result
    return df

def show_distribution_of_attributes(df, bins=40, figsize=(12,8)):
    %matplotlib inline
    df.hist(bins=bins, figsize=figsize)
    plt.show()