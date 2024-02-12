from twilio_ import WhatsappMessage
from open_ai_message import TextCreator
import random
import time
from datetime import datetime

partner_name = input("What is your Partner's name \n")
your_name = input("What is your name \n")


def execute_command():
    random_number = round(random.uniform(0.1, 0.99), 2)
    message_body = TextCreator(your_name=your_name, partner_name=partner_name, temperature=random_number)
    send_message = WhatsappMessage(message_body=message_body)
    send_message.send_message()


today = datetime.now()
if today.month == 2 and today.day == 14:
    for _ in range(10):
        if random.random() < 0.5:
            execute_command()
            time.sleep(random.uniform(0.5, 3) * 3600)
