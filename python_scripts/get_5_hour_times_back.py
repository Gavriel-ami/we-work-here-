import pandas as pd
from datetime import datetime, timedelta

# Define the original data
data = {
    'Max Date': [
        '6/6/2024 14:00', '6/6/2024 14:00', '6/6/2024 14:00', '6/6/2024 14:00', '6/6/2024 14:00',
        '6/6/2024 13:00', '6/6/2024 13:00', '6/6/2024 13:00', '6/6/2024 13:00', '6/6/2024 13:00',
        '6/6/2024 12:00', '6/6/2024 12:00', '6/6/2024 12:00', '6/6/2024 12:00', '6/6/2024 12:00',
        '6/6/2024 11:00', '6/6/2024 11:00', '6/6/2024 11:00', '6/6/2024 11:00', '6/6/2024 11:00',
        '6/6/2024 10:00', '6/6/2024 10:00', '6/6/2024 10:00', '6/6/2024 10:00', '6/6/2024 10:00',
        '6/6/2024 9:00', '6/6/2024 9:00', '6/6/2024 9:00', '6/6/2024 9:00', '6/6/2024 9:00'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Get the current time
current_time = datetime.now()

# Iterate through the DataFrame and adjust times
for i in range(len(df)):
    hours_to_subtract = (i // 5)
    df.at[i, 'Max Date'] = current_time - timedelta(hours=hours_to_subtract)

print(df)
