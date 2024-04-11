import pandas as pd

def explore_categorical_columns(df):
    return df.select_dtypes("object").columns

def explore_numerical_columns(df):
    return df.select_dtypes("int64").columns

def missing_values_check(df):
    if df.isnull().sum().sum()==0:
        print("there is no missing value")
    else:
        print("there are missing values")


