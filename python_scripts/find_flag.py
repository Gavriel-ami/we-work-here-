import os
import pandas as pd
import sys 

from filter_folders import get_sorted_folders
from read_until_empty_row import read_until_first_empty_row 
from datetime import datetime

def reformat_date(date_str: str) -> str:
    """
    Reformat a date string from 'YYYY-MM-DD hh:mm AM/PM' to 'YYYY-MM-DD hh:mm:ss'.
    Args:
    date_str (str): The date string to reformat.
    Returns:
    str: The reformatted date string.
    """
    # Original date format
    original_format = "%Y-%m-%d %I:%M %p"
    # Desired date format
    new_format = "%Y-%m-%d %H:%M:%S"
    
    # Parse the original date string into a datetime object
    datetime_obj = datetime.strptime(date_str, original_format)
    # Format the datetime object into the new format
    reformatted_date_str = datetime_obj.strftime(new_format)
    
    return reformatted_date_str

def check_dante(df,how_came_first):
    was_a_dante = []
    for i in range(df.shape[0]):
        date_part = df['Max Date'][i].strftime('%Y-%m-%d')
        # Combine date part with 'Max' and 'Min' times as strings
        max_str = f"{date_part} {df['Max'][i]}"
        min_str = f"{date_part} {df['Min'][i]}"
        max_date_str = df['Max Date'][i].strftime('%Y-%m-%d %I:%M %p')
        # Convert the combined strings back to datetime for comparison
        max_datetime = pd.to_datetime(max_str)
        min_datetime = pd.to_datetime(min_str)
        reformatted_max_date_str = reformat_date(max_date_str)
        # make a dection how to test min or max . 
        if how_came_first[i][0] == 'Min':
            #      Max Date         vs          min 
            if reformatted_max_date_str == (str(min_datetime)):
                # print("Max Date == to min, there is no dante")
                was_a_dante.append((how_came_first[i],False))
            else:
                was_a_dante.append((how_came_first[i],True))
                # print(f"there is a dante {str(min_datetime)} : {str(reformatted_max_date_str)}")

        elif how_came_first[i][0] == 'Max':
            #      Max Date         vs          max
            if reformatted_max_date_str == (str(max_datetime)):
                # print("Max == to max Date,there is no dante")
                was_a_dante.append((how_came_first[i],False))
            else:
                # print("there is a dante")
                was_a_dante.append((how_came_first[i],True))
    return was_a_dante

def get_trend_and_how_came_first(df):
    df_old = df
    list_of_how_came_first = []
    for i in range(df_old.shape[0]):
        date_part = df_old['Max Date'][i].strftime('%Y-%m-%d')
        # Combine date part with 'Max' and 'Min' times as strings
        max_str = f"{date_part} {df_old['Max'][i]}"
        min_str = f"{date_part} {df_old['Min'][i]}"
        max_date_str = df_old['Max Date'][i].strftime('%Y-%m-%d %I:%M %p')
        # Convert the combined strings back to datetime for comparison
        max_datetime = pd.to_datetime(max_str)
        min_datetime = pd.to_datetime(min_str)
       
        came_first = ""
        # Determine which time came first or if they are equal
        if max_datetime < min_datetime:
            came_first += f"Max"
        elif max_datetime > min_datetime:
            came_first += f"Min"
        else:
            came_first += f"Max and Min are equal"
        list_of_how_came_first.append((came_first,i)) # adding how came first into a list
        
    # print('list_of_how_came_first', list_of_how_came_first)
    ################### get trends up/down ##################################### 
    old_df_trends = []
    # Iterate over the given list and replace 'Min' with 'up_trend' and 'Max' with 'down_trend'
    for item, index in list_of_how_came_first:
        if item == 'Min':
            old_df_trends.append(('up_trend', index))
        elif item == 'Max':
            old_df_trends.append(('down_trend', index))
    #### get the trend (up or down) and how came first #######
    return old_df_trends,list_of_how_came_first 

def get_df(folder_name):
    #### get the df  - df_old #######
    # Specify the folder name and the file name
    file_name = f'{folder_name}_Batch_Control.xlsx'
    print(file_name)
    file_path = os.path.join(folder_name, file_name)
    df = read_until_first_empty_row(file_path)
    # print(df)
    return df

def find_all_false_to_true_indexes(old_list, new_list):
    indexes = []  # Initialize an empty list to store the indexes
    
    # Iterate over both lists simultaneously using enumerate and zip
    for i, (old_item, new_item) in enumerate(zip(old_list, new_list)):
        # Check if the old list has True and the new list has False at the same index
        if old_item[1] == True and new_item[1] == False:
            indexes.append(i)  # Append the index to the list

    return indexes 

def compare_dante_changes(old_list,new_list):
    # # Example usage REMOVE THIS IN prodaction 
    # old_list = [(('Max', 0), False), (('Max', 1), True), (('Max', 2), True), (('Max', 3), True), (('Max', 4), True), (('Max', 5), True), (('Min', 6), False), (('Min', 7), False)]
    # new_list = [(('Max', 0), True), (('Max', 1), True), (('Max', 2), True), (('Max', 3), True), (('Max', 4), True), (('Max', 5), True), (('Min', 6), True), (('Min', 7), True)]

    # # Example usage REMOVE THIS IN PRODACTION 
    indexes = find_all_false_to_true_indexes(old_list, new_list)
    print(f"Indexes where old list is False and new list is True: {indexes}")
    return indexes

def comper_new_vs_old(was_a_dante_df_old,was_a_dante_df_new):
    # Comper new vs old. 
    indexes_places = compare_dante_changes(was_a_dante_df_old,was_a_dante_df_new)
    if (len(indexes_places) != 0):
        print("there is a flag of change.")
        print(f"{indexes_places}")
        return indexes_places
    else:
        print('no flag found yet')
    return 

# def get_args(x,y):
#     x = sys.args[0]
#     y = sys.args[1]
#     return x,y 



def main():

    # x,y = get_args()

    new, old , sorted_folder = get_sorted_folders()
    print(new)
    df_old  = get_df(old) # get the old file df 
    df_new  = get_df(new) # get the new file df 

    # old 
    old_df_trends,old_list_of_how_came_first = get_trend_and_how_came_first(df_old)
    was_a_dante_df_old = check_dante(df_old,old_list_of_how_came_first)
    print(was_a_dante_df_old)
    print("")
    # new 
    new_df_trends,new_list_of_how_came_first = get_trend_and_how_came_first(df_new)
    was_a_dante_df_new = check_dante(df_new,new_list_of_how_came_first)
    print(was_a_dante_df_new)

    # Comper new vs old
    indexes_places = comper_new_vs_old(was_a_dante_df_old,was_a_dante_df_new)

    # To do :
    # save this into a file ! , and after the next time it would just add up not delte the old one . 
    if indexes_places:
        # Print the selected rows and columns
        # print(df_new.columns)
        columns_to_keep = ['DT ', 'Tindex Duplicate  Point','Max Date'] # add min or max and max date.
        print(df_new.loc[indexes_places, columns_to_keep])
        sliced_df = df_new.loc[indexes_places, columns_to_keep]
        sliced_df['batch_folder'] = new
        # Check if the file already exists
        file_exists = os.path.isfile('flags_output.csv')
        # Write the sliced DataFrame to a CSV file (append if it exists)
        sliced_df.to_csv('flags_output.csv', mode='a', header=not file_exists, index=False)
        print("DataFrame slice has been appended to 'flags_output.csv'")





if __name__ == '__main__':
    main()


    