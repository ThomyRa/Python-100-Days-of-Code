import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPH_ID = "graph01"
headers = {
    "X-USER-TOKEN": TOKEN
}
####################################################
# CREATING USER

# user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)


####################################################
# CREATING GRAPH

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Meditation Graph",
#     "unit": "Mins",
#     "type": "int",
#     "color": "sora"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

####################################################
# ADDING PIXEL

# pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime.datetime.now()
# pixel_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "20",
# }
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

####################################################
# UPDATING A PIXEL

today = datetime.datetime.now()
print(today.strftime("%Y%m%d"))
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
print(update_endpoint)
update_pixel_conf = {
    "quantity": "60",
}
response = requests.put(url=update_endpoint, json=update_pixel_conf, headers=headers)
print(response.text)
