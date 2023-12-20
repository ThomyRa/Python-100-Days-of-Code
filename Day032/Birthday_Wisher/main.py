import pandas as pd
import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv


random_template = random.choice(os.listdir("./letter_templates/"))
letters_path = f"./letter_templates/{random_template}"
with open(str(letters_path), "r") as file:
    letter_content = file.readlines()

birthdays_df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
for (idx, row) in birthdays_df.iterrows():
    if row["month"] == now.month and row["day"] == now.day:
        letter_contents = "".join(letter_content).replace("[NAME]", row["name"])

        load_dotenv()
        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("PASSWORD")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject: Happy Birthday\n\n{letter_contents}")
