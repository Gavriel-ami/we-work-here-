import shutil
import os

def copy_file_to_destination(source, destination_dir, filename):
    """
    Copies a file from source to destination directory with a new filename.

    Args:
    - source (str): Full path to the source file.
    - destination_dir (str): Directory where the file should be copied.
    - filename (str): New filename for the copied file.

    Returns:
    - bool: True if the file was copied successfully, False otherwise.
    """
    # Print out paths for debugging
    print(f"Source: {source}")
    print(f"Destination Directory: {destination_dir}")

    # Check if the source file exists
    if not os.path.exists(source):
        print(f"Error: Source file '{source}' not found.")
        return False
    
    # Construct the full destination path
    destination = os.path.join(destination_dir, filename)

    # Check if the destination file already exists and delete it if so
    if os.path.exists(destination):
        try:
            os.remove(destination)
            print(f"Existing file '{destination}' deleted.")
        except Exception as e:
            print(f"Error: Failed to delete existing file '{destination}': {e}")
            return False

    try:
        # Copy the file from source to destination
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}'.")
        return True
    except PermissionError:
        print(f"Error: Permission denied when copying file to '{destination}'.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    source = r"C:\Users\Owner\source\repos\amiMultClient\amiMultClient\bin\Debug\net8.0\python_scripts\flags_output.csv"
    destination_dir = r"C:\Users\Owner\source\repos\amiMultClient\amiMultClient\bin\Debug\net8.0\python_scripts"
    filename = "flags_output_new.csv"

    # Call the function to copy the file
    success = copy_file_to_destination(source, destination_dir, filename)

    if success:
        print("File copy operation completed successfully.")
    else:
        print("File copy operation failed.")

if __name__ == "__main__":
    main()
