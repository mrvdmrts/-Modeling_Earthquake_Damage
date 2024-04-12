import pandas as pd

def load_data(file_path:str) ->pd.DataFrame:
    """Loads data from csv file into DataFrame

    Args:
        file_path (str): file path

    Returns:
        pd.DataFrame
    """
    df = pd.read_csv(file_path)
    return df
