import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv


def send_email():
    load_dotenv()
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    destination_email = os.getenv("DESTINATION_EMAIL")
    with open("./quotes.txt") as file:
        quotes_list = file.readlines()

    quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=destination_email,
                            msg=f"Subject: Monday Motivation\n\n{quote}")


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    send_email()
