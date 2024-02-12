import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CORTEX_API_KEY")


class TextCreator:
    def __init__(self, your_name, partner_name, temperature):
        API_KEY = api_key
        self.payload = {
            "formality": "default",
            "max_tokens": 2048,
            "model": "gpt-3.5-turbo-16k",
            "n": 1,
            "source_lang": "en",
            "target_lang": "en",
            "temperature": temperature,
            "text": f"create a happy valentine text for my girlfriend. My name is {your_name} and {partner_name} name is Natasha."
        }
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        self.url = "https://api.textcortex.com/v1/texts/completions"

    def create_text(self):
        make_request = requests.request(
            method="POST",
            url=self.url,
            json=self.payload,
            headers=self.headers
        )
        response = make_request.json()
        if response["status"] == "success":
            return response["data"]["outputs"][0]["text"]
        else:
            return "I'm sorry, but there was an error generating the love message. I still love you though."


