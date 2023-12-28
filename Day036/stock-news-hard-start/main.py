import requests
from prettyprinter import pprint
from dotenv import load_dotenv
import os

STOCK = "AMD"
COMPANY_NAME = "ADVANCED MICRO DEVICES, INC."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
# pprint(data)
data_list = [value for (key, value) in data['Time Series (Daily)'].items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data['4. close']

print(yesterday_closing_price, before_yesterday_closing_price)