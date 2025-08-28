import os
import shutil
import sys

def move_folder(folder_name, destination_path):
    # Get the script directory (one folder back from where the script is run)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the source folder path
    source_folder = os.path.join(script_dir, folder_name)

    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    # Ensure the destination directory exists, create it if not
    if not os.path.exists(destination_path):
        print(f"Destination directory '{destination_path}' does not exist. Creating...")
        os.makedirs(destination_path)

    try:
        # Move the specified folder to the destination
        shutil.move(source_folder, destination_path)
        print(f"Folder '{folder_name}' moved to '{destination_path}'.")
    except Exception as e:
        print(f"An error occurred while moving the folder: {e}")

if __name__ == "__main__":
    # Set the destination path
    destination_path = r"C:\Users\Owner\Documents\old_runs"

    # Check if folder name is provided as command-line argument
    if len(sys.argv) > 1:
        folder_name = sys.argv[1]
    else:
        print("Usage: python script_name.py folder_name")
        sys.exit(1)

    # Call the function to move the folder
    move_folder(folder_name, destination_path)
