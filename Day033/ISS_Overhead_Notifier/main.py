import requests
import datetime as dt
import smtplib
from dotenv import load_dotenv
import os
import time
from prettyprinter import pprint

MY_LAT = 5.067680
MY_LONG = -75.509819


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()

    if sunset < time_now.hour < sunrise:
        return True


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


while True:
    time.sleep(60)
    print("Checking if the ISS is close to my location...")
    if is_iss_overhead() and is_dark():
        load_dotenv()
        print("ISS is in the Sky!!")
        my_email = os.getenv("MY_EMAIL")
        my_password = os.getenv("MY_PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=my_email,
                password=my_password
            )
            connection.sendmail(
                from_addr=my_email,
                to_addrs="thomy.tests@outlook.com",
                msg="ISS is in the Sky\n\nHeyy o/ \nLook up, the ISS is in the sky."
            )
