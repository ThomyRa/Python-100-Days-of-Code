from bs4 import BeautifulSoup
import requests
from prettyprinter import pprint
import lxml
import smtplib
from dotenv import load_dotenv
import os

URL = "https://www.amazon.com/BINNUNE-Microphone-Playstation-Headphones-Cancelling/dp/B096VRK6J5/133-4732069-7769535"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept-Language": "en-US,en;q=0.5",
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
pprint(price)

if price <= 35:
    load_dotenv()
    message = f"Subject:Alert Low Price🚨🏷️\nLow price in this product on Amazon:\n\n{URL}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=os.getenv("MY_EMAIL"),
            password=os.getenv("PASSWORD"),
        )
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"),
            to_addrs=os.getenv("MY_EMAIL"),
            msg=message.encode("utf8")
        )
