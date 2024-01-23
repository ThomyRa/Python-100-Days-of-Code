from bs4 import BeautifulSoup
import requests
from prettyprinter import pprint
import lxml

URL = "https://www.amazon.com/BINNUNE-Microphone-Playstation-Headphones-Cancelling/dp/B096VRK6J5/133-4732069-7769535"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept-Language": "en-US,en;q=0.5",
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
# pprint(soup)

price = soup.find(class_="a-offscreen").getText().split("$")[1]
pprint(price)

