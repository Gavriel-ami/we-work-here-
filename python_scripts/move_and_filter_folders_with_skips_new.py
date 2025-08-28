import os
import re
import shutil
import datetime
import sys

DATE_FORMAT = '%Y%m%d'
ORG_DATE_FORMAT = '%m-%d-%Y'
FOLDER_PATTERN = re.compile(r'^\d+_\d+$')

def filter_folders(folder_names):
    """
    Filter folder names to include only those that match the pattern 'digits_digits'.
    Args:
        folder_names (list): List of folder names.
    Returns:
        list: Filtered list of folder names.
    """
    filtered_folders = [folder for folder in folder_names if FOLDER_PATTERN.match(folder)]
    print(f"Filtered folders: {filtered_folders}")
    return filtered_folders

def move_folders_to_path(folder_names, destination_path, parent_directory):
    """
    Move specified folders to the destination path.
    Args:
        folder_names (list): List of folder names to be moved.
        destination_path (str): Destination path where the folders will be moved.
    """
    source_path = parent_directory

    for folder in folder_names:
        source = os.path.join(source_path, folder)
        destination = os.path.join(destination_path, folder)
        print(f"Moving '{source}' to '{destination}'")
        try:
            # Check if source and destination are on the same drive
            if os.path.splitdrive(source)[0] != os.path.splitdrive(destination)[0]:
                print(f"Source and destination are on different drives. Moving without commonpath check.")
                shutil.move(source, destination)
                print(f"Moved folder '{folder}' to '{destination}'")
            else:
                if not os.path.commonpath([source, destination]).startswith(source):
                    shutil.move(source, destination)
                    print(f"Moved folder '{folder}' to '{destination}'")
                else:
                    print(f"Skipping moving '{folder}' into itself")
        except PermissionError:
            print(f"Skipping folder '{folder}' - Permission Denied")
        except shutil.Error as e:
            print(f"Skipping folder '{folder}' - {e}")

def organize_folders_by_date(source_dir):
    """
    Organize folders in the source directory by their date prefixes.
    Args:
        source_dir (str): The source directory containing the folders to organize.
    """
    dest_dir = os.path.join(source_dir, 'organized_runs')
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Organizing folders in '{source_dir}' into '{dest_dir}'")

    for folder_name in os.listdir(source_dir):
        folder_path = os.path.join(source_dir, folder_name)
        print(f"Checking '{folder_path}'")
        if os.path.isdir(folder_path) and folder_name != 'organized_runs':
            try:
                date_str = folder_name.split('_')[0]
                date_obj = datetime.datetime.strptime(date_str, DATE_FORMAT)
                dest_folder_name = date_obj.strftime(ORG_DATE_FORMAT)
                dest_folder_path = os.path.join(dest_dir, dest_folder_name)
                print(f"Destination folder path: '{dest_folder_path}'")

                # Check if source and destination are on the same drive
                if os.path.splitdrive(folder_path)[0] != os.path.splitdrive(dest_folder_path)[0]:
                    print(f"Source and destination are on different drives. Moving without commonpath check.")
                    os.makedirs(dest_folder_path, exist_ok=True)
                    shutil.move(folder_path, os.path.join(dest_folder_path, folder_name))
                    print(f"Moved folder '{folder_name}' to '{dest_folder_name}'")
                else:
                    if not os.path.commonpath([folder_path, dest_folder_path]).startswith(folder_path):
                        os.makedirs(dest_folder_path, exist_ok=True)
                        shutil.move(folder_path, os.path.join(dest_folder_path, folder_name))
                        print(f"Moved folder '{folder_name}' to '{dest_folder_name}'")
                    else:
                        print(f"Skipping moving '{folder_name}' into itself")
            except ValueError:
                print(f"Skipping folder '{folder_name}' - Not in expected format 'YYYYMMDD_HHMMSS'")
            except PermissionError:
                print(f"Skipping folder '{folder_name}' - Permission Denied")
            except shutil.Error as e:
                print(f"Skipping folder '{folder_name}' - {e}")

    print("All folders have been reorganized into folders by date.")

def move_and_filter_flow(destination_path):
    """
    Execute the process of filtering and moving folders, then organizing them by date.
    Args:
        destination_path (str): Path to move the folders to.
    """
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))
    print(f"Execute from the Parent directory: ********************* '{parent_directory}'\n")
    print("Destination path:", destination_path)
    print("")

    folders = [folder for folder in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, folder))]
    print("Before filtering folders:", folders)

    filtered_folders = filter_folders(folders)
    print("Filtered folders:", filtered_folders)
    print("Filtered folders count:", len(filtered_folders))
    move_folders_to_path(filtered_folders, destination_path, parent_directory)
    organize_folders_by_date(destination_path)

def main(destination_path=None):
    if destination_path:
        print("Destination Path:", destination_path)
        move_and_filter_flow(destination_path)
    else:
        print("Usage: python move_and_filter_folders.py DESTINATION_PATH")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        destination_path = sys.argv[1]
        main(destination_path)
    else:
        main()