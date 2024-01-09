from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_URL")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_URL")


class DataManager:

    def __init__(self):
        self.headers = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers,
            )
            # print(response.text)

    def get_user_emails(self):
        email_list = []
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        for row in data["users"]:
            email_list.append(row["email"])

        print(email_list)
        return email_list
