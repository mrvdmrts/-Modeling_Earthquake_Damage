import pandas as pd

def create_training_data(df_train, df_label) :
    data = pd.merge(df_train, df_label, on='building_id')
    return data.iloc[:, 1: -1].values, data['damage_grade']