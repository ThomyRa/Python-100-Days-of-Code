import os
from dotenv import load_dotenv
import requests
from prettyprinter import pprint
from datetime import datetime

NUTRIX_BASE_URL = "https://trackapi.nutritionix.com"
NUTRIX_END_POINT = "/v2/natural/exercise"

load_dotenv()
NUTRI_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRI_APP_ID = os.getenv("NUTRITIONIX_APP_ID")

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

user_input = input("Insert exercise: ")
parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

NUTRIX_URL = f"{NUTRIX_BASE_URL}{NUTRIX_END_POINT}"
nutrix_response = requests.post(url=NUTRIX_URL, json=parameters, headers=headers)
nutrix_response.raise_for_status()
pprint(nutrix_response.json())
nutrix_data = nutrix_response.json()

SHEETY_URL = os.getenv("SHEETY_URL")
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": os.getenv("SHEETY_TOKEN")
}
for exercise in nutrix_data["exercises"]:
    sheet_row = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_URL, json=sheet_row, headers=headers)
    print(sheet_response.text)
