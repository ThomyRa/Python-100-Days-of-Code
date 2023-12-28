import requests
from prettyprinter import pprint
from dotenv import load_dotenv
import os
from twilio.rest import Client

STOCK = "AMD"
COMPANY_NAME = "ADVANCED MICRO DEVICES, INC."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
# pprint(stock_data)
data_list = [value for (key, value) in stock_data['Time Series (Daily)'].items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 5:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles'][:3]
    pprint(articles)
    formatted_articles = [f"{COMPANY_NAME}: {up_down}{diff_percent}\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18589476263",
            to="+573028548550"
        )
        print(message.status)
