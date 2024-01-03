# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

flight_deals_sheet = DataManager()
flight_search = FlightSearch()
sheet_data = flight_deals_sheet.get_excel_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

    flight_deals_sheet.destination_data = sheet_data
    flight_deals_sheet.update_destination_codes()
# cities = flight_deals_sheet.get_cities()
# codes = FlightSearch("manizales")
# codes.get_code()
# print(codes)


