from twilio.rest import Client
import os
from dotenv import load_dotenv
from data_manager import DataManager
import smtplib

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("VIRTUAL_PHONE")
TWILIO_VERIFIED_NUMBER = os.getenv("TO_PHONE")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("PASSWORD")

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message):

        data_manager = DataManager()
        emails = data_manager.get_user_emails()

        for email in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(
                    user=self.email,
                    password=self.password
                )
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"New Deal  🚨📢🏷️🛒\n{message}".encode("utf8")
                )
