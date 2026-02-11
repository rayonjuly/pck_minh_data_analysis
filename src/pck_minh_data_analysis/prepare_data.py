import pandas as pd
import re
from unidecode import unidecode


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

import operator
from functools import reduce

def pd_and(*args):
    """
    Combines multiple pandas conditions using bitwise AND (&).
    Usage: df[pd_and(cond1, cond2, cond3, ...)]
    """

    return reduce(operator.and_, args)

def pd_or(*args):
    """
    Combines multiple pandas conditions using bitwise OR (|).
    Usage: df[pd_or(cond1, cond2, cond3)]
    """
    return reduce(operator.or_, args)