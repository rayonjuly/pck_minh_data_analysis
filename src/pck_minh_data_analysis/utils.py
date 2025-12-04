import pandas as pd
import re
from unidecode import unidecode

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