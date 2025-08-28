# import pandas as pd
# import sys
# from datetime import datetime

# def read_csv(file_path):
#     try:
#         # Read the CSV file
#         df = pd.read_csv(file_path)
        
#         # Display the DataFrame
#         return df
#     except Exception as e:
#         print(f"Error reading the CSV file: {e}")
#         return None

# def get_only_today_date(df):
#     try:
#         # Get today's date
#         today = datetime.today().date()
        
#         # Convert the 'Max Date' column to datetime
#         df['Max Date'] = pd.to_datetime(df['Max Date'])
        
#         # Filter the DataFrame to include only rows with today's date
#         df_today = df[df['Max Date'].dt.date == today]
        
#         return df_today
#     except Exception as e:
#         print(f"Error filtering by today's date: {e}")
#         return None

# def replace_trend_labels(df):
#     try:
#         # Create a copy of the DataFrame to avoid SettingWithCopyWarning
#         df_copy = df.copy()
        
#         # Define a function to map trend labels to symbols
#         def map_trend_to_symbol(trend):
#             if trend.startswith("('up_trend'"):
#                 return '↗'
#             elif trend.startswith("('down_trend'"):
#                 return '↘'
#             else:
#                 return trend  # Return the original value if not 'up_trend' or 'down_trend'
        
#         # Apply the mapping function to the 'Flag_Trend' column
#         df_copy['Flag_Trend'] = df_copy['Flag_Trend'].apply(lambda x: map_trend_to_symbol(x))
        
#         return df_copy
#     except Exception as e:
#         print(f"Error replacing trend labels: {e}")
#         return None

# def write_to_excel(df, output_file):
#     try:
#         # Drop 'batch_folder' column if present
#         if 'batch_folder' in df.columns:
#             df.drop(columns=['batch_folder'], inplace=True)
        
#         # Create a Pandas Excel writer
#         with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
#             # Write DataFrame to Excel sheet 'Filtered Data'
#             df.to_excel(writer, sheet_name='Filtered Data', index=False)
            
#             # Auto-adjust column widths
#             worksheet = writer.sheets['Filtered Data']
#             for idx, col in enumerate(df):
#                 max_len = max(df[col].astype(str).map(len).max(), len(col)) + 1
#                 worksheet.set_column(idx, idx, max_len)
            
#         print(f"Filtered data saved to {output_file}")
#     except Exception as e:
#         print(f"Error writing to Excel file: {e}")

# def main():
#     # Check if a file path was provided
#     if len(sys.argv) != 2:
#         print("Usage: python clean_flag.py <file_path>")
#         sys.exit(1)
    
#     file_path = sys.argv[1]
    
#     # Read the CSV file
#     df = read_csv(file_path)
    
#     if df is not None:
#         # Filter the DataFrame by today's date
#         df_today = get_only_today_date(df)
        
#         if df_today is not None:
#             # Replace trend labels
#             df_today = replace_trend_labels(df_today)
            
#             # Display the filtered DataFrame
#             print(df_today)
#             print(df_today.shape)
            
#             output_file = "./filtered_data.xlsx"  # Change this path if needed
#             write_to_excel(df_today, output_file)

#         else:
#             print("Error occurred while filtering by today's date.")
#     else:
#         print("Error occurred while reading the CSV file.")

# if __name__ == '__main__':
#     main()



import pandas as pd
import sys
from datetime import datetime
import os
import shutil



def read_csv(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Display the DataFrame
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def get_only_today_date(df):
    try:
        # Get today's date
        today = datetime.today().date()
        
        # Convert the 'Max Date' column to datetime
        df['Max Date'] = pd.to_datetime(df['Max Date'])
        
        # Filter the DataFrame to include only rows with today's date
        df_today = df[df['Max Date'].dt.date == today]
        
        return df_today
    except Exception as e:
        print(f"Error filtering by today's date: {e}")
        return None

def replace_trend_labels(df):
    try:
        # Create a copy of the DataFrame to avoid SettingWithCopyWarning
        df_copy = df.copy()
        
        # Define a function to map trend labels to symbols
        def map_trend_to_symbol(trend):
            if trend.startswith("('up_trend'"):
                return '↗'
            elif trend.startswith("('down_trend'"):
                return '↘'
            else:
                return trend  # Return the original value if not 'up_trend' or 'down_trend'
        
        # Apply the mapping function to the 'Flag_Trend' column
        df_copy['Flag_Trend'] = df_copy['Flag_Trend'].apply(lambda x: map_trend_to_symbol(x))
        
        return df_copy
    except Exception as e:
        print(f"Error replacing trend labels: {e}")
        return None

def write_to_excel(df, output_file):
    try:
        # Drop 'batch_folder' column if present
        if 'batch_folder' in df.columns:
            df.drop(columns=['batch_folder'], inplace=True)
        
        # Create a Pandas Excel writer
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            # Write DataFrame to Excel sheet 'Filtered Data'
            df.to_excel(writer, sheet_name='Filtered Data', index=False)
            
            # Get the xlsxwriter workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets['Filtered Data']
            
            # Define formats for green (↗) and red (↘) symbols
            green_format = workbook.add_format({'font_color': '#008000'})  # Green color
            red_format = workbook.add_format({'font_color': '#FF0000'})    # Red color
            
            # Auto-adjust column widths
            for idx, col in enumerate(df):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 1
                worksheet.set_column(idx, idx, max_len)
            
            # Loop through each cell in the 'Flag_Trend' column starting from the second row (index 1)
            for row_num, value in enumerate(df['Flag_Trend'], start=1):
                # Apply green format for '↗' and red format for '↘'
                if value == '↗':
                    worksheet.write(row_num, df.columns.get_loc('Flag_Trend'), value, green_format)
                elif value == '↘':
                    worksheet.write(row_num, df.columns.get_loc('Flag_Trend'), value, red_format)
        
        print(f"Filtered data saved to {output_file}")
    except Exception as e:
        print(f"Error writing to Excel file: {e}")

def main():
    # Check if a file path was provided
    if len(sys.argv) != 2:
        print("Usage: python clean_flag.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print("this is the file path:",file_path)
    # Read the CSV file
    df = read_csv(file_path)
    
    if df is not None:
        # Filter the DataFrame by today's date
        df_today = get_only_today_date(df)
        
        if df_today is not None:
            # Replace trend labels
            df_today = replace_trend_labels(df_today)
            
            # Display the filtered DataFrame
            print(df_today)
            print(df_today.shape)
            
            output_file = "./filtered_data.xlsx"  # Change this path if needed
            write_to_excel(df_today, output_file)

        else:
            print("Error occurred while filtering by today's date.")
    else:
        print("Error occurred while reading the CSV file.")

if __name__ == '__main__':
    main()
