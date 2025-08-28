import pandas as pd

def update_excel_column(input_file, sheet_name, column_name, tindex_values):
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


def update_excel_column1(input_file, sheet_name, column_name, dt_values):
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


# Example usage:
input_file = 'Batch_Control_History.xlsx'
sheet_name = 'Control Sheet'
column_name = 'Tindex Duplicate  Point'
tindex_values = [1.7,1.75,1.8,1.85,1.9]

update_excel_column(input_file, sheet_name, column_name, tindex_values)

# Example usage:
column_name = 'DT '
dt_values = [0.0001, 0.0002, 0.0003] # need to do a fix for this over the intire file . 

update_excel_column1(input_file, sheet_name, column_name, dt_values)
number_of_hours = 6 
tindex_values_size = len(tindex_values)
total_times = number_of_hours*tindex_values_size
print(total_times) 
# build a new list with the total_times for every obj in the dt_value list . 
# 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 ,  * total_times

# then send the new list into func  update_excel_column1 insted . 

def build_big_dt_values_list(dt_values,total_times):
    # build the bid list using the dt_values list and the total_times and return it back .


# [0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 ,
#  0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 ,
#  0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 , 0.0001 ] 
    return big_dt_values