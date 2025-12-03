import pandas as pd

def show_null_values(df):
    df_no_null_values = df.isna().sum().rename('Num of null rows')
    df_pct_null_values = (df.isna().sum() * 100/ len(df)).round(4).rename('PCT of null rows')

    result = pd.concat(
        [df_no_null_values, df_pct_null_values]
        , axis=1
    )

    return result