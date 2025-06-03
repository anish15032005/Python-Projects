import requests
from datetime import datetime

MY_LAT = 26.449923
MY_LNG = 80.331871

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # Use 0 for ISO 8601 format (UTC)
    "date": "today"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0]) 
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0]) 

time_now = datetime.now()
print(time_now)