from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("TWILIO_PHONE_NUMBER")
partner_number = os.getenv("PARTNER_PHONE_NUMBER")


class WhatsappMessage:
    def __init__(self, message_body):
        ACCOUNT_SID = account_sid
        AUTH_TOKEN = auth_token
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        self.body = message_body

    def send_message(self):
        message = self.client.messages.create(
            to=f"whatsapp:{partner_number}",
            from_=f"whatsapp:{phone_number}",
            body=self.body
        )
        return message.sid
