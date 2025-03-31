import pandas as pd

def input_from_console():
    """Reads text input from the console"""
    return input("Please enter text: ")

def input_from_file(filename):
    """Reads a text file using Python's built-in capabilities"""
    with open(filename, 'r') as file:
        return file.read()

def input_from_file_pandas(filename):
    """Reads the contents of a file using the pandas library"""
    df = pd.read_csv(filename)
    return df.to_string()
