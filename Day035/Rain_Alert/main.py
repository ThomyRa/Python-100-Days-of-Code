import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
OPW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OPW_API_KEY")
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')


parameters = {
    "lat": 5.067680,
    "lon": -75.509819,
    "appid": api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get(OPW_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body="It's going to rain. Remeber to bring and umbrella.☂️",
                from_='+19282385222',
                to='+573028548550'
        )
    print(message.status)

