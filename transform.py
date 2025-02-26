import pandas as pd

def add_column(df, col_name, col_data):
    """
    This function adds a column to a dataframe.
    """
    df[col_name] = col_data
    return df

def filter_by_quality(df, condition, lower=False):
    """
    This function filters a dataframe based on a condition.
    """
    if lower:
        return df[df["quality"] <= condition]
    else:
        return df[df["quality"] >= condition]

def count_avarage_alcohol(df):
    """
    This function computes the average alcohol content for a dataframe.
    """
    return df['alcohol'].mean()