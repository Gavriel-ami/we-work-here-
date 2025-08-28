import os
import pandas as pd

def read_until_first_empty_row(file_path):
    try:
        # Read the entire Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        # Find the first index where all elements are NaN
        first_empty_index = df[df.isnull().all(axis=1)].index.min()
        
        if pd.isna(first_empty_index):
            # If there's no fully empty row, return the entire DataFrame
            return df
        else:
            # Return the DataFrame up to the first all-NaN row
            return df.loc[:first_empty_index-1]
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return pd.DataFrame()
