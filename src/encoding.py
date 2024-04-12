from sklearn.preprocessing import LabelEncoder

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