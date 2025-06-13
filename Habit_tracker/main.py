import requests
from datetime import datetime
pixele_endpoint = "https://pixe.la/v1/users"
USERNAME = "enter_your_username_here"  # Replace with your Pixela username
TOKEN = "update_your_token_here"  # Replace with your Pixela token
# Create a user account on Pixela
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixele_endpoint, json=user_params)
print(response.text)


graph_endpoint = f"{pixele_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color":"ajisai",
    "timezone": "Asia/Kolkata"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

pixel_creation_endpoint = f"{pixele_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
today_date = today.strftime("%Y%m%d")



pixel_data = {
    "date": today_date,
    "quantity": input("How many kilometers did you cycle today? "),
}
update_endpoint = f"{pixele_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
new_pixel_data = {
    "quantity": "12.5",
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers={"X-USER-TOKEN": TOKEN})
print(response.text)

#Delete a pixel
delete_endpoint = f"{pixele_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
response2 = requests.delete(url=delete_endpoint, headers={"X-USER-TOKEN": TOKEN})
print(response2.text)