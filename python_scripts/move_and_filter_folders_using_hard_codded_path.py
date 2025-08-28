import os
import re 
import shutil
import datetime


DESTINATION_PATH = r'C:\Users\Owner\Documents\old_runs'

def organize_folders_by_date(source_dir):
    # Create destination directory if it doesn't exist
    dest_dir = os.path.join(source_dir, 'organized_runs')
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over folders in the source directory
    for folder_name in os.listdir(source_dir):
        # Get full path of the folder
        folder_path = os.path.join(source_dir, folder_name)
        
        # Check if the path is a directory
        if os.path.isdir(folder_path):
            # Try to parse the folder name as a datetime object
            try:
                # Extract date information from the folder name
                date_str = folder_name.split('_')[0]  # Assuming YYYYMMDD format
                date_obj = datetime.datetime.strptime(date_str, '%Y%m%d')
                
                # Create destination directory with "MM-DD-YYYY" format
                dest_folder_name = date_obj.strftime('%m-%d-%Y')
                dest_folder_path = os.path.join(dest_dir, dest_folder_name)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(dest_folder_path):
                    os.makedirs(dest_folder_path)
                
                # Move the source folder to the destination folder
                dest_folder = os.path.join(dest_folder_path, folder_name)
                shutil.move(folder_path, dest_folder)
                
                print(f"Moved folder '{folder_name}' to '{dest_folder_name}'")
            
            except ValueError:
                print(f"Skipping folder '{folder_name}' - Not in expected format 'YYYYMMDD_HHMMSS'")

    print("All folders have been reorganized into folders by date.")

def move_folders_to_path(folder_names, DESTINATION_PATH):
    """
    Move folders from the parent directory of the current working directory to a specified destination path.

    Args:
        folder_names (list): List of folder names to be moved.
        DESTINATION_PATH (str): Destination path where the folders will be moved.
    """
    # Get the parent directory of the current working directory
    source_path = os.path.abspath(os.path.join(os.getcwd(), '..'))

    # Move each folder to the destination path
    for folder in folder_names:
        # Get the absolute path of the folder
        source = os.path.join(source_path, folder)
        # Construct the destination path for the folder
        destination = os.path.join(DESTINATION_PATH, folder)
        # Move the folder to the destination path
        shutil.move(source, destination)
        print(f"Moved folder '{folder}' to '{destination}'")

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
    return filtered_folders


# FILTER FOLDERS 
# Get the parent directory path (one level up)
parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
# Get a list of all folders in the parent directory (one folder up)
folders = [folder for folder in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, folder))]
print("BEFOR filtering folders:",folders)
filtered_folders = filter_folders(folders)
print("")
print("filtered folders:",filtered_folders)
print("filtered folders length:",len(filtered_folders))

# MOVE FOLDERS 
move_folders_to_path(filtered_folders, DESTINATION_PATH)
path_to_order = DESTINATION_PATH
organize_folders_by_date(path_to_order)


# using args 
# import os
# import re 
# import shutil
# import datetime
# import sys

# def organize_folders_by_date(source_dir, destination_path):
#     # Create destination directory if it doesn't exist
#     dest_dir = os.path.join(source_dir, 'organized_runs')
#     if not os.path.exists(dest_dir):
#         os.makedirs(dest_dir)

#     # Iterate over folders in the source directory
#     for folder_name in os.listdir(source_dir):
#         # Get full path of the folder
#         folder_path = os.path.join(source_dir, folder_name)
        
#         # Check if the path is a directory
#         if os.path.isdir(folder_path):
#             # Try to parse the folder name as a datetime object
#             try:
#                 # Extract date information from the folder name
#                 date_str = folder_name.split('_')[0]  # Assuming YYYYMMDD format
#                 date_obj = datetime.datetime.strptime(date_str, '%Y%m%d')
                
#                 # Create destination directory with "MM-DD-YYYY" format
#                 dest_folder_name = date_obj.strftime('%m-%d-%Y')
#                 dest_folder_path = os.path.join(dest_dir, dest_folder_name)

#                 # Create the destination folder if it doesn't exist
#                 if not os.path.exists(dest_folder_path):
#                     os.makedirs(dest_folder_path)
                
#                 # Move the source folder to the destination folder
#                 dest_folder = os.path.join(dest_folder_path, folder_name)
#                 shutil.move(folder_path, dest_folder)
                
#                 print(f"Moved folder '{folder_name}' to '{dest_folder_name}'")
            
#             except ValueError:
#                 print(f"Skipping folder '{folder_name}' - Not in expected format 'YYYYMMDD_HHMMSS'")

#     print("All folders have been reorganized into folders by date.")

# def move_folders_to_path(folder_names, destination_path):
#     """
#     Move folders from the parent directory of the current working directory to a specified destination path.

#     Args:
#         folder_names (list): List of folder names to be moved.
#         destination_path (str): Destination path where the folders will be moved.
#     """
#     # Get the parent directory of the current working directory
#     source_path = os.path.abspath(os.path.join(os.getcwd(), '..'))

#     # Move each folder to the destination path
#     for folder in folder_names:
#         # Get the absolute path of the folder
#         source = os.path.join(source_path, folder)
#         # Construct the destination path for the folder
#         destination = os.path.join(destination_path, folder)
#         # Move the folder to the destination path
#         shutil.move(source, destination)
#         print(f"Moved folder '{folder}' to '{destination}'")

# def filter_folders(folder_names):
#     """
#     Filter folder names to include only those that start with a number and end with a number.
#     Args:
#         folder_names (list): List of folder names.
#     Returns:
#         list: Filtered list of folder names.
#     """
#     # Regular expression pattern to match folder names starting and ending with a number
#     pattern = re.compile(r'^\d+\_\d+$')
#     # Filter folder names using the pattern
#     filtered_folders = [folder for folder in folder_names if pattern.match(folder)]
#     return filtered_folders


# if __name__ == "__main__":
#     # Check if the destination path argument is provided
#     if len(sys.argv) < 2:
#         print("Usage: python script_name.py DESTINATION_PATH")
#         sys.exit(1)
    
#     # Get the destination path from command-line arguments
#     DESTINATION_PATH = sys.argv[1]

#     # FILTER FOLDERS 
#     # Get the parent directory path (one level up)
#     parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..'))
#     # Get a list of all folders in the parent directory (one folder up)
#     folders = [folder for folder in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, folder))]
#     print("BEFORE filtering folders:", folders)
#     filtered_folders = filter_folders(folders)
#     print("")
#     print("Filtered folders:", filtered_folders)
#     print("Filtered folders length:", len(filtered_folders))

#     # MOVE FOLDERS 
#     move_folders_to_path(filtered_folders, DESTINATION_PATH)
#     path_to_order = DESTINATION_PATH
#     organize_folders_by_date(path_to_order, DESTINATION_PATH)
