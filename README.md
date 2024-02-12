# A Valentine WhatsApp Auto-Texting Script

This is a simple Python script created to help send random text messages using GPT-3.5 Turbo via WhatsApp.

## Usage

To use this script, follow these steps:

1. Clone the repository:
```commandline
git clone https://github.com/huelight/a-valentine-whatsapp-auto-texting-app.git
```

2. Install the required dependencies:
```commandline
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and fill it with the necessary environment variables:

```env
CORTEX_API_KEY=cortexAPI
TWILIO_ACCOUNT_SID=twilio_account_sid
TWILIO_AUTH_TOKEN=twilio_auth_token
PARTNER_PHONE_NUMBER=your_partners_number
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

You can get your `CORTEX_API_KEY` from [TextCortex](https://textcortex.com/text-generation-api) and your Twilio `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` from [Twilio Console](https://www.twilio.com/console).

To activate the Twilio sandbox for messaging on WhatsApp:

1. Go to your [Twilio Console](https://www.twilio.com/console).
2. Navigate to Messaging > Send a message.
3. Activate the sandbox by sending a message on WhatsApp.
4. Once activated, you will see your phone number. Also, activate the phone number you want to send the message to.

Once the .env file is filled in correctly, you can run the script:
```commandline
python main.py
```

## Improvements and Suggestions
Ideas to make the code better or increase its implementability are welcome. Feel free to contribute by opening issues or pull requests.