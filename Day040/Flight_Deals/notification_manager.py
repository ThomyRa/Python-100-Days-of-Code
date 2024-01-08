from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("5e6cf9ffd27f8bd90f9b59f6c93b6a28")
TWILIO_VIRTUAL_NUMBER = "+18589476263"
TWILIO_VERIFIED_NUMBER = os.getenv("TO_PHONE")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
