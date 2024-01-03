import os
from dotenv import load_dotenv
import requests
from prettyprinter import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    BASE_URL = "https://api.tequila.kiwi.com/"

    def __init__(self):
        load_dotenv()
        base_url = "https://api.tequila.kiwi.com"
        # self.city = city
        self.TEQ_SEARCH_URL = f"{base_url}/locations/query"
        self.headers = {
            "apikey": os.getenv("TEQUILA_API_KEY")
        }
        self.parameters = {
            # "term": self.city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": True,
            "sort": "sort",
        }

    def get_code(self, city_name: str):
        code = "TESTING"
        return code
        # response = requests.get(
        #     url=self.TEQ_SEARCH_URL,
        #     params=self.parameters,
        #     headers=self.headers,
        # )
        # pprint(response.json())
