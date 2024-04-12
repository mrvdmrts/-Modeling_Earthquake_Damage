import pandas as pd
def submit(df, y):
    """ Creating csv file with submission format

    Args:
        df (DataFrame): Test DataFrame
        y (list): Predicted values
    """
    building_ids = df.iloc[:, 0].values
    df_submission = pd.DataFrame({"building_id" : building_ids, "damage_grade" : y})
    df_submission.to_csv("data/submission.csv", index=False)