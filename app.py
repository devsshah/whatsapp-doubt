from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio credentials (set these as environment variables on Render)
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM_WHATSAPP = 'whatsapp:+14155238886'  # Twilio sandbox number

# Your second WhatsApp number (added to the WhatsApp group)
TO_WHATSAPP_NUMBER = os.environ.get('TO_WHATSAPP_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/incoming', methods=['POST'])
def handle_message():
    body = request.form.get('Body')
    sender = request.form.get('From')

    # Forward message to your second WhatsApp number
    client.messages.create(
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP_NUMBER,
        body=f"📩 Anonymous Doubt:
{body}"
    )

    # Send confirmation back to the sender
    client.messages.create(
        from_=FROM_WHATSAPP,
        to=sender,
        body="✅ Your doubt has been shared anonymously with the group!"
    )

    return 'OK', 200

if __name__ == '__main__':
    app.run()