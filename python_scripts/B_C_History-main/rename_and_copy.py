# import os
# import shutil

# def rename_file_and_copy(src_path, dest_dir, new_name):
#     # Ensure the destination directory exists
#     os.makedirs(dest_dir, exist_ok=True)
    
#     # Define the destination file path
#     dest_path = os.path.join(dest_dir, new_name)
#     print("destion path:",dest_path)
#     # Check if the destination file already exists and remove it if it does
#     if os.path.exists(dest_path):
#         os.remove(dest_path)
    
#     # Copy the source file to the destination directory and rename it
#     shutil.copy(src_path, dest_path)






import os
import shutil

def rename_file_and_copy(src_file, dest_directory, new_file_name):
    # Ensure the path uses raw strings or double backslashes
    dest_directory = dest_directory.rstrip("\\")
    
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_directory, exist_ok=True)
    
    # Construct the full destination path
    dest_file = os.path.join(dest_directory, new_file_name)
    
    # Copy the file to the new location
    shutil.copy(src_file, dest_file)












# # Define the source file path, destination directory, and new file name
# src_file = r'C:\Users\Owner\source\repos\amiMultClient\amiMultClient\bin\Debug\net8.0\python_scripts\B_C_History-main\_Batch_Control_History_template.xlsx'
# dest_directory = r'C:\Users\Owner\source\repos\amiMultClient\amiMultClient\bin\Debug\net8.0'
# new_file_name = "Batch_Control_History.xlsx"

# # Call the function to rename the file
# rename_file(src_file, dest_directory, new_file_name)
