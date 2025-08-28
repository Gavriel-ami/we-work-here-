import os
import pandas as pd

def read_the_batch_history_file(input_file):
    parent_directory = os.getcwd()
    complete_path = os.path.join(parent_directory, input_file)
    # Read the Excel file into a DataFrame
    df = pd.read_excel(complete_path)
    # Find the index of the first empty row
    first_empty_index = df.index[df.isnull().all(axis=1)].min()

    # Check if first_empty_index is a valid integer index
    if pd.notna(first_empty_index):
        # Slice the DataFrame up to (but not including) the first empty row
        df_until_empty = df.iloc[:int(first_empty_index)]
        # Optionally, print or use df_until_empty here
        print("Sliced DataFrame up to the first empty row:")
        # print(df_until_empty)
        df = df_until_empty
    else:
        print("No empty row found in the DataFrame.")
    return df
