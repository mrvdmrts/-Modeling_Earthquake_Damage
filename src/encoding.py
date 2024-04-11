from sklearn.preprocessing import LabelEncoder

def encoding(df_train, df_test):
    le = LabelEncoder()
    col = df_train.select_dtypes("object").columns
    for c in col:
        le.fit(df_train[c])
        # Fit and transform the categorical data in train set
        df_train[c]=le.transform(df_train[c])
        # Fit and transform the categorical data in test set
        df_test[c]=le.transform(df_test[c])
        return df_train, df_test