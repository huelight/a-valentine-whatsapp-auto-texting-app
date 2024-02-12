from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("TWILIO_PHONE_NUMBER")
partner_number = os.getenv("PARTNER_PHONE_NUMBER")


class WhatsappMessage:
    """Class to handle WhatsApp messages"""
    def __init__(self, message_body):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, self.auth_token)
        self.body = message_body

    def send_message(self):
        """Send a WhatsApp message"""
        message = self.client.messages.create(
            to=f"whatsapp:{partner_number}",
            from_=f"whatsapp:{phone_number}",
            body=self.body
        )
        return message.sid
