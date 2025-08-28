import pandas as pd

# Load the existing Excel file
input_file = 'Batch_Control_History.xlsx'
df_existing = pd.read_excel(input_file, sheet_name='Control Sheet')
print(df_existing.columns)
# Define the list of 'Tindex Duplicate Point' values
tindex_values = [1.6,1.65,1.7, 1.75, 1.8, 1.85,1.9]

# Ensure the DataFrame has the 'Tindex Duplicate Point' column and update it
if 'Tindex Duplicate  Point' in df_existing.columns:
    # Calculate the number of times tindex_values will repeat
    num_repeats = len(df_existing) // len(tindex_values) + 1
    
    # Generate the cyclic values for 'Tindex Duplicate Point'
    updated_values = tindex_values * num_repeats
    
    # Update the 'Tindex Duplicate Point' column directly
    df_existing['Tindex Duplicate  Point'] = updated_values[:len(df_existing)]
else:
    raise ValueError("Column 'Tindex Duplicate Point' not found in the DataFrame.")

# Save the updated DataFrame back to the Excel file
df_existing.to_excel(input_file, index=False, sheet_name='Control Sheet')

print("Updated 'Tindex Duplicate Point' column in Batch_Control_History.xlsx.")
