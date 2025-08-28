import sys
import os
import pandas as pd 
import termcolor
import pyfiglet
import datetime
from pandas import read_excel
from datetime import datetime


def zero_seconds(datetime_str):
    """
    Takes a datetime string and returns it with seconds and microseconds set to 00.

    Args:
    datetime_str (str): The input datetime string.

    Returns:
    str: The output datetime string with seconds and microseconds set to 00.
    """
    try:
        # Try parsing with microseconds
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        # Fallback to parsing without microseconds
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    # Set seconds and microseconds to zero
    dt_zeroed = dt.replace(second=0, microsecond=0)

    # Return the zeroed datetime as a string in the required format
    return dt_zeroed.strftime("%Y-%m-%d %H:%M:%S")

def send_error():
    # Create big text using pyfiglet
    big_text = pyfiglet.figlet_format("ERROR In Data", font="slant")
    # Print the big text in red
    print(termcolor.colored(big_text, "red"))
    # Print an additional bold message
    print(termcolor.colored("The data is WRONG!", "red", attrs=["bold"]))

def test_sheet_over_max_date(file_name,my_sheet):
    df = read_excel(file_name, sheet_name = 'Control Sheet')
    df2 = read_excel(file_name, sheet_name = my_sheet)
    first_time = str(df['Max Date'][0]) # first page  - Control Sheet - time
    second_time = df2['datetime'].iloc[int(df['Algo Input Minutes'][0]-2)]
    print('')
    
    first_time = zero_seconds(first_time)
    
    if first_time == second_time :
        print(f"Max Date: {first_time} Vs {second_time }")
    elif first_time != second_time :

        print('first_time', first_time)
        print('second_time', second_time)
        send_error()
        print("The data is Bad ! ! !   There is somthing Wrong with the data !!!")
        return True
    return False

def get_second_sheet_name(excel_path):
    excel_file = pd.ExcelFile(excel_path)
    return excel_file.sheet_names[1]

def get_full_path(file_name):
    return os.getcwd() +"\\" + file_name

def read_batch(filename):
    file_name = filename  # change it to the name of your excel file
    full_path = get_full_path(file_name)
    print(f'{full_path}')
    my_sheet = get_second_sheet_name(full_path)

    print('File name:', file_name)
    print('Second sheet name:', my_sheet)

    df = read_excel(file_name, sheet_name = my_sheet)
    test_len(df,my_sheet)

    # new function
    answer = test_sheet_over_max_date(file_name,my_sheet)

    if answer:
        return 
    interval = find_intervales(df)
    print('interval', interval)

    skip_rows, skip_differences = find_skips(interval, df)
    
    print("")
    print("Rows with skips:", [x + 2 for x in skip_rows])
    print("Actual time differences for skips:", skip_differences)
    print("")
    print("Amount of skips:", len(skip_rows))
    return 
    
def test_len(df,my_sheet):
    
    if (len(df.datetime)) != 399:
        print(f"There is somthing Wrong with the data !!! look at the amount of rows of the Batch control in sheet name:{my_sheet}")
        sys.exit(1)

def find_intervales(df):
    df['datetime'] = pd.to_datetime(df['datetime'])
    # Calculate the difference between the datetime values of the first and second rows
    difference_timedelta = df.iloc[[1]]['datetime'].values[0] - df.iloc[[0]]['datetime'].values[0]
    difference_timedelta_python = pd.Timedelta(difference_timedelta)
    interval = int(difference_timedelta_python.total_seconds() / 60)
    second_interval = int(pd.Timedelta(df.iloc[[2]]['datetime'].values[0] - df.iloc[[1]]['datetime'].values[0]).total_seconds() / 60)

    if interval == second_interval :
        # we have the the right interval. 
        return interval
    elif interval != second_interval : 
        try:
            print("An error occurred:", str(e))
            raise RuntimeError("No data found. Exiting program.")
        except Exception as e:
            return

def find_skips(interval_minutes, df):
    """
    Find skips in time intervals between consecutive rows in a DataFrame.

    Parameters:
    - interval_minutes (int): The specified interval in minutes.
    - df (pandas.DataFrame): The DataFrame containing a 'datetime' column.

    Returns:
    - skip_rows (list): List of row numbers where skips occurred.
    - skip_differences (list): List of actual time differences corresponding to skips.
    """
    # Convert 'datetime' column to datetime objects if not already done
    if not pd.api.types.is_datetime64_any_dtype(df['datetime']):
        df['datetime'] = pd.to_datetime(df['datetime'])

    # Sort the DataFrame by datetime column
    df = df.sort_values(by='datetime')

    # Convert interval from minutes to timedelta
    interval_timedelta = pd.Timedelta(minutes=interval_minutes)

    # Initialize lists to store row numbers and actual time differences
    skip_rows = []
    skip_differences = []

    # Iterate through rows and find skips
    for i in range(1, len(df)):
        time_difference = df.iloc[i]['datetime'] - df.iloc[i - 1]['datetime']
        if time_difference != interval_timedelta:
            skip_rows.append(i)  # Store row number
            skip_differences.append(time_difference)  # Add 2 to the time difference

    return skip_rows, skip_differences

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 batch_tester.py <xyz12341234_Batch_Control.xlsx>")
        sys.exit()

    filename = sys.argv[1]
    print(filename)
    read_batch(filename)

if __name__ == "__main__":
    main()