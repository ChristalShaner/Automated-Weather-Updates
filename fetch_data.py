import os
import requests
import json
import pandas as pd
from datetime import datetime


api_key = "90fd33a30323bbaaa4067637530f9a54"  # make sure it's valid
cities = ["Kiev", "Mexico City", "Dublin"]

data_list = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract temperature information from the response
    temperature = data["main"]["temp"]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"The temperature in {city} is {temperature} Kelvin.")
    data_list.append({"City": city, "Temperature": temperature, "Timestamp": current_time})

    

df = pd.DataFrame(data_list)

existing_csv_file = "temperature_data.csv"

# Check if the CSV file exists
if not os.path.isfile(existing_csv_file) or os.stat(existing_csv_file).st_size == 0:
    # If the file doesn't exist or is empty, write the header
    df.to_csv(existing_csv_file, index=False)
else:
    # If the file exists and is not empty, append the data along with the header
    df.to_csv(existing_csv_file, mode="a", header = False,index=False)

print(f"Data appended to {existing_csv_file}")
