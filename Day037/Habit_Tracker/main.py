import os

import requests
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": "graph01",
    "name": "Meditation Graph",
    "unit": "Mins",
    "type": "int",
    "color": "sora"
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)