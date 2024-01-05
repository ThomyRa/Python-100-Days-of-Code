import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):

        load_dotenv()
        self.ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
        self.TO_PHONE = os.getenv('TO_PHONE')

    def send_sms(self, message: str):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_="+18589476263",
            to=self.TO_PHONE
        )
        print(message.sid)



