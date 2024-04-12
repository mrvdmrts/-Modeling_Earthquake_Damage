import pandas as pd
def submit(df, y):
    building_ids = df.iloc[:, 0].values
    df_submission = pd.DataFrame({"building_id" : building_ids, "damage_grade" : y})
    df_submission.to_csv("data/submission.csv", index=False)