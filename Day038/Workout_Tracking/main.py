import os
from dotenv import load_dotenv
import requests
from prettyprinter import pprint

NUTRIX_BASE_URL = "https://trackapi.nutritionix.com"
NUTRIX_END_POINT = "/v2/natural/exercise"

load_dotenv()
NUTRI_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRI_APP_ID = os.getenv("NUTRITIONIX_APP_ID")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

parameters = {
    "query": "Run 5 Kms"
}

NUTRIX_URL = f"{NUTRIX_BASE_URL}{NUTRIX_END_POINT}"
response = requests.post(url=NUTRIX_URL, json=parameters, headers=headers)
response.raise_for_status()
pprint(response.json())

