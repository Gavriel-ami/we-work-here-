import os
import shutil
import pandas as pd
from datetime import datetime, timedelta
from pandas.errors import EmptyDataError
import sys 
import ast




def generate_dates(start_datetime, hours_back, tindex_values, num_rows):
    generated_dates = []
    total_iterations = hours_back * len(tindex_values)
    current_datetime = start_datetime

    while len(generated_dates) < num_rows:
        for i in range(hours_back):
            current_datetime = start_datetime - timedelta(hours=i)
            for tindex in tindex_values:
                generated_dates.append(current_datetime.strftime('%m/%d/%Y %H:%M'))
                if len(generated_dates) >= num_rows:
                    return generated_dates

    # If the number of dates is less than num_rows, repeat the last date
    while len(generated_dates) < num_rows:
        generated_dates.append(generated_dates[-1])

    return generated_dates[:num_rows]

def update_max_date_column(excel_file_path, sheet_name, column_name, new_dates):
    try:
        # Try reading the Excel file with pandas
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        
        # Check if the column exists
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in sheet '{sheet_name}'")
        
        # Ensure the new_dates list has the same length as the DataFrame
        if len(new_dates) != len(df):
            raise ValueError("Length of new_dates does not match the number of rows in the DataFrame.")

        # Update the 'Max Date' column with new values
        df[column_name] = new_dates
        
        # Save the updated DataFrame back to Excel
        with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            workbook = writer.book
            worksheet = writer.sheets[sheet_name]
            date_format = workbook.add_format({'num_format': 'mm/dd/yyyy hh:mm'})
            
            # Apply the date format to the 'Max Date' column
            for row in range(1, len(new_dates) + 1):
                worksheet.write_datetime(row, df.columns.get_loc(column_name), datetime.strptime(new_dates[row - 1], '%m/%d/%Y %H:%M'), date_format)

        print(f"'Max Date' column updated successfully in {excel_file_path}.")
        
    except EmptyDataError:
        print("Error: The file is empty or cannot be read.")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def update_excel_column(input_file, sheet_name, column_name, dt_values):
    # Load the existing Excel file
    df_existing = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Ensure the DataFrame has the specified column and update it
    if column_name in df_existing.columns:
        # Calculate the number of times dt_values will repeat
        num_repeats = len(df_existing) // len(dt_values) + 1
        
        # Generate the cyclic values for the column
        updated_values = dt_values * num_repeats
        
        # Update the column directly
        df_existing[column_name] = updated_values[:len(df_existing)]
    else:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
    
    # Save the updated DataFrame back to the Excel file
    df_existing.to_excel(input_file, index=False, sheet_name=sheet_name)
    
    print(f"Updated '{column_name}' column in {input_file}.")

def generate_big_tindex_values(tindex_values, size_of_value):
    big_tindex_values = []
    for value in tindex_values:
        big_tindex_values.extend([value] * size_of_value)
    return big_tindex_values

def update_excel_column_on_tindex(input_file, sheet_name, column_name, tindex_values):
    # Load the existing Excel file
    df_existing = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Ensure the DataFrame has the specified column and update it
    if column_name in df_existing.columns:
        # Calculate the number of times tindex_values will repeat
        num_repeats = len(df_existing) // len(tindex_values) + 1
        
        # Generate the cyclic values for the column
        updated_values = tindex_values * num_repeats
        
        # Update the column directly
        df_existing[column_name] = updated_values[:len(df_existing)]
    else:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")
    
    # Save the updated DataFrame back to the Excel file
    df_existing.to_excel(input_file, index=False, sheet_name=sheet_name)
    
    print(f"Updated '{column_name}' column in {input_file}.")

def copy_file(file_name):
    # Define the source file path
    source_file = os.path.abspath(file_name)

    # Construct the destination path - three folders back
    destination_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Define the full path for the copied file in the destination
    destination_file = os.path.join(destination_dir, os.path.basename(source_file))

    # Copy the file
    shutil.copy2(source_file, destination_file)

    print(f"File copied to: {destination_file}")


def main():

    #Default values
    default_tindex_values = [1.75, 1.8, 1.85, 1.9]
    default_hours_back_to_test = 6
    default_dt_values = [0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009]

    # Check if arguments are provided
    if len(sys.argv) > 1:
        tindex_values = ast.literal_eval(sys.argv[1])
        hours_back_to_test = int(sys.argv[2])
        dt_values = ast.literal_eval(sys.argv[3])
    else:
        tindex_values = default_tindex_values
        hours_back_to_test = default_hours_back_to_test
        dt_values = default_dt_values



    # Variables
    # tindex_values = [1.75 ,1.8, 1.85, 1.9] # 
 

    HOURS_BACK_TO_TEST = 6
    # EXCEL_FILE_PATH = r'C:\projects\AMI WE WORK HERE\AmiMult\python_scripts\b_c_h\Batch_Control_History.xlsx'
    EXCEL_FILE_PATH = r'C:\AMI WE WORK HERE\AmiMult\python_scripts\b_c_h\Batch_Control_History.xlsx'
    SHEET_NAME = 'Control Sheet'
    COLUMN_NAME = 'Max Date'

    # Generate new dates
    start_datetime = datetime.now()
    df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=SHEET_NAME)
    num_rows = len(df)
    new_dates = generate_dates(start_datetime, HOURS_BACK_TO_TEST, tindex_values, num_rows)

    # Update the new_dates at Excel file 
    # Set  ****** Max Date ******
    update_max_date_column(EXCEL_FILE_PATH, SHEET_NAME, COLUMN_NAME, new_dates)


    # Set ****** DT ****** values:
    input_file = 'Batch_Control_History.xlsx'
    COLUMN_NAME = 'DT '
    # dt_values = [0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007, 0.0008, 0.0009] # 
    hours_back_to_test = 6

    size_of_value = len(tindex_values) * hours_back_to_test
    big_dt_values = generate_big_tindex_values(dt_values, size_of_value)
    print(big_dt_values)
    print(len(big_dt_values))
    update_excel_column(input_file, SHEET_NAME, COLUMN_NAME, big_dt_values)
    

    # Set ****** Tindex Duplicate  Point ****** values:
    input_file = 'Batch_Control_History.xlsx'
    sheet_name = 'Control Sheet'
    column_name = 'Tindex Duplicate  Point'

    update_excel_column_on_tindex(input_file, sheet_name, column_name, tindex_values)
  
    copy_file('Batch_Control_History.xlsx')


if __name__ == "__main__":
    main()
