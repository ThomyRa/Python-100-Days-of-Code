import os
from dotenv import load_dotenv
import requests
from prettyprinter import pprint


class DataManager:
    def __init__(self):
        load_dotenv()
        self.destination_data = {}
        self.SHEETY_URL = os.getenv("SHEETY_URL")
        self.headers = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }

    def get_excel_data(self) -> list:
        response = requests.get(url=self.SHEETY_URL, headers=self.headers)
        response.raise_for_status()
        sheet_data = response.json()
        self.destination_data = sheet_data["prices"]
        return sheet_data["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_URL}/{city['id']}",
                json=new_data,
                headers=self.headers,
            )
            response.raise_for_status()
            print(response.text)
