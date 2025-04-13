# Anonymous WhatsApp Doubt Bot

This bot receives private WhatsApp messages and forwards them anonymously to a group using a second WhatsApp number.

## Setup Steps

1. Create a Twilio account and activate the WhatsApp Sandbox.
2. Add your environment variables:
   - `ACCOUNT_SID`
   - `AUTH_TOKEN`
   - `TO_WHATSAPP_NUMBER` (e.g., whatsapp:+91xxxxxxxxxx)
3. Deploy on Render.com (use this repo).
4. Set your Twilio Sandbox webhook to `https://<your-app>.onrender.com/incoming`
5. Add your second WhatsApp number to the group and use AutoResponder for forwarding.

Done!