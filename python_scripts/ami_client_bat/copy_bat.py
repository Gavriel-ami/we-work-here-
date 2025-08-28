import sys
import os
import shutil

def copy_and_replace_file(src_file, dest_dir):
    # Check if the source file exists
    if not os.path.isfile(src_file):
        print(f"Source file does not exist: {src_file}")
        return

    # Check if the destination directory exists
    if not os.path.isdir(dest_dir):
        print(f"Destination directory does not exist: {dest_dir}")
        return

    # Construct the destination file path
    file_name = os.path.basename(src_file)
    dest_file_path = os.path.join(dest_dir, file_name)

    try:
        # If the file already exists in the destination directory, remove it
        if os.path.isfile(dest_file_path):
            os.remove(dest_file_path)
            print(f"Old file removed: {dest_file_path}")

        # Copy the new file to the destination directory
        shutil.copy(src_file, dest_file_path)
        print(f"File copied successfully to {dest_file_path}.")
    except Exception as e:
        print(f"Failed to copy file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy_and_replace_file.py <src_file> <dest_dir>")
    else:
        src_file = sys.argv[1]
        dest_dir = sys.argv[2]
        copy_and_replace_file(src_file, dest_dir)
