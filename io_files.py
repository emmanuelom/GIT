import pandas as pd

def read_csv_as_dataframe(file_path):
    """
    Reads a CSV file and returns it as a pandas DataFrame.
    
    :param file_path: Path to the CSV file.
    :return: pandas DataFrame containing the CSV data.
    """
    return pd.read_csv(file_path)

def write_dataframe_to_csv(dataframe, file_path, index=False):
    """
    Writes a pandas DataFrame to a CSV file.
    
    :param dataframe: pandas DataFrame to write.
    :param file_path: Path to save the CSV file.
    :param index: Whether to write row indices to the file. Default is False.
    """
    dataframe.to_csv(file_path, index=index)

def foo():
    pass