import shutil
# Function to copy the file within the same folder
def copy_file_to_same_folder(input_file):
    """
    Copy a file into the same folder.

    Parameters:
        input_file (str): Path to the input file.

    Returns:
        str: Path to the copied file.
    """
    # Copy the file into the same folder
    file_copy_named =  "_" +input_file  
    shutil.copy(input_file, file_copy_named)
    return input_file, file_copy_named

# input_file = 'Batch_Control_History_template.xlsx'
# copy_file_to_same_folder(input_file)