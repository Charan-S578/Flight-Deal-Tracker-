from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

class NotificationManager:
    def send_sms(self, message):
        # This class is respondible for dending notification with the deal flight details.
        client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )

        message = client.messages.create(
            body=message,
            from_="TWILIO_PHONE_NUMBER",
            to="MY_PHONE_NUMBER",
        )

        print(message.sid)