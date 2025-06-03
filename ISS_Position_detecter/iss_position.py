import requests
from datetime import datetime
MY_LAT = 26.449923  # Your latitude
MY_LONG = 80.331871  # Your longitude

def is_iss_overhead():
    response= requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    data = response.json()  # Parse the JSON response

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    iss_position = (iss_longitude, iss_latitude)
    # print(iss_position)  # Output the ISS position
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # Use 0 for ISO 8601 format (UTC)
    }

    #Your position is within +5 or -5 degrees of the ISS position.
    if 21 <= iss_latitude <= 31 and 75 <= iss_longitude <= 85:
        return True
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])  # Extract hour from sunrise
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])  # Extract hour from sunset
    time_now = datetime.now().hour  # Get current hour (0-23)
    
    if time_now >= sunset or time_now <= sunrise:
        return True

#send a notification if the ISS is overhead and it's night time
while True:
    if is_iss_overhead() and is_night():
        print("Look up! The ISS is overhead and it's night time.")


# print(response)
#Expalining the status codes
#1XX: Hold On
#2XX: Here You Go
#3XX: Go Away
#4XX: You messed up
#5XX: I(Server) messed up
#Find more at: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# print(response.status_code) #200

# if response.status_code != 200:
#     raise Exception("Error: API request unsuccessful.")

# if response.status_code == 404:
#     raise Exception("Error: Page not found.")

# if response.status_code == 401:
#     raise Exception("Error: Unauthorized access.")



#if the ISS is close to my current position and it is currently dark
#Then send me an email to tell me to look up.
#Run the code every 60 seconds


