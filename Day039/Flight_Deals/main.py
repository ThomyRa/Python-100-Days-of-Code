# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY = "BOG"

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_excel_data()
print(type(sheet_data))

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        origin=ORIGIN_CITY,
        destination=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
