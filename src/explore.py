import pandas as pd

def explore_categorical_columns(df):
    """Showing categorical columns

    Args:
        df (DataFrame): DataFrame

    Returns:
        list: categorical columns
    """
    return df.select_dtypes("object").columns

def explore_numerical_columns(df):
     """Showing numerical columns

    Args:
        df (DataFrame): DataFrame

    Returns:
        list: numerical columns
    """
     return df.select_dtypes("int64").columns

def missing_values_check(df):
    """Checking missing values

    Args:
        df (DataFrame): DataFrame
    """
    if df.isnull().sum().sum()==0:
        print("there is no missing value")
    else:
        print("there are missing values")


