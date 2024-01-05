import os
from dotenv import load_dotenv
import requests
from prettyprinter import pprint
from datetime import datetime
from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        load_dotenv()
        self.BASE_URL = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": os.getenv("TEQUILA_API_KEY")
        }

    def get_destination_code(self, city_name: str) -> str:
        teq_location_url = f"{self.BASE_URL}/locations/query"
        parameters = {
            "term": city_name,
            "location_types": "city",
            "limit": "1",
            "locale": "es-ES"
        }
        response = requests.get(
            url=teq_location_url,
            params=parameters,
            headers=self.headers,
        )
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        pprint(code)
        return code

    def search_flights(self, origin: str, destination: str,
                       from_time: datetime, to_time: datetime):
        teq_search_url = f"{self.BASE_URL}/v2/search"
        query = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "COP"
        }
        response = requests.get(url=teq_search_url, params=query, headers=self.headers)
        try:
            data = response.json()["data"][0]
            # pprint(data)
        except IndexError:
            print(f"No flights found for {destination}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
