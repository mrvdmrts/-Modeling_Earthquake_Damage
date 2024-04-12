from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def encoding(df_train, df_test):
    """Encoding function for categorical features

    Args:
        df_train (Data Frame): Train data
        df_test (Data Frame): Test data

    Returns:
        DataFrames: Encoded data Frames 
    """
    le = LabelEncoder()
    for c in df_train.select_dtypes("object").columns:
        le.fit(df_train[c])
        # Fit and transform the categorical data in train set
        df_train[c]=le.transform(df_train[c])
        # Fit and transform the categorical data in test set
        df_test[c]=le.transform(df_test[c])

    return df_train, df_test

def one_hot_encoding(df_train,df_test):

    one_hot_encoder=OneHotEncoder()
    one_hot_encoded_data_train = pd.get_dummies(df_train, columns = df_train.select_dtypes('object').columns)
    one_hot_encoded_data_test = pd.get_dummies(df_test, columns = df_test.select_dtypes('object').columns)
    return one_hot_encoded_data_train,one_hot_encoded_data_test