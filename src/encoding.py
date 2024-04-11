from sklearn.preprocessing import LabelEncoder
from src.explore import explore_categorical_columns

def encoding(df_train, df_test):
    le = LabelEncoder()
    col = df_train.select_dtypes("object").columns
    print(col)
    """for c in col:
        le.fit(df_train[c])
        # Fit and transform the categorical data in train set
        df_train[c]=le.transform(df_train[c])
        # Fit and transform the categorical data in test set
        df_test[c]=le.transform(df_test[c])
    return df_train, df_test"""