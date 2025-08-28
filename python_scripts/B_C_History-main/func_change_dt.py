import pandas as pd

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

# Example usage:
input_file = 'Batch_Control_History_1.xlsx'
sheet_name = 'Sheet1'# Control 
column_name = 'DT '
dt_values = [0.0001, 0.0002, 0.0003, 0.0004,0.0005]

update_excel_column(input_file, sheet_name, column_name, dt_values)
