import requests
from datetime import date, datetime

USERNAME = "pythonerik"
TOKEN = "theflume"
GRAPH_ID = "theflume111"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# responce = requests.post(url=pixela_endpoint, json=user_params)
# print(responce)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# responce = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(responce.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today= datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes of code did you do today?"),
}

responce = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(responce.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "164",
}

# responce = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(responce.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

delete_pixel_data = {}

# responce = requests.delete(url=delete_endpoint, json=delete_pixel_data, headers=headers)
# print(responce.text)