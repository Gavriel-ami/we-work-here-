import os
import re 
import pandas as pd 


def filter_folders(folder_names):
    """
    Filter folder names to include only those that start with a number and end with a number.
    Args:
        folder_names (list): List of folder names.
    Returns:
        list: Filtered list of folder names.
    """
    # Regular expression pattern to match folder names starting and ending with a number
    pattern = re.compile(r'^\d+\_\d+$')
    # Filter folder names using the pattern
    filtered_folders = [folder for folder in folder_names if pattern.match(folder)]
    print(filtered_folders)
    return filtered_folders

def get_sorted_folders():

    # FILTER FOLDERS 
    # Get the parent directory path (one level up)
    parent_directory = os.path.abspath(os.path.join(os.getcwd()))
    # Get a list of all folders in the parent directory (one folder up)
    folders = [folder for folder in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, folder))]
    # print("BEFOR filtering folders:",folders)
    filtered_folders = filter_folders(folders)

    sorted_folders = sorted(filtered_folders, key=lambda x: int(x.split('_')[-1]))
    # print('sorted_folders', sorted_folders)
    # print('new', sorted_folders[-1]) # newer folder
    # print('old', sorted_folders[-2]) # older the newer folder  
    new =  sorted_folders[-1]
    old =  sorted_folders[-2]

    return new , old , sorted_folders   

# read the old file and test if there is a bamp or not at the old 
# read the new file and see if there is a line (up or max ) .

