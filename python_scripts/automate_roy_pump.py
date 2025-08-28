import requests
import time

# URL to call
url = "http://www.roie.com/Ds/Set_Pump_Frequency.asp?Freq=2"

# Function to call the page
def call_page():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Page called successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Error calling the page at {time.strftime('%Y-%m-%d %H:%M:%S')}: Status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error calling the page at {time.strftime('%Y-%m-%d %H:%M:%S')}: {e}")

# Interval in seconds (120 minutes)
interval = 120 * 60

# Call the page every 120 minutes indefinitely
while True:
    call_page()
    time.sleep(interval)
