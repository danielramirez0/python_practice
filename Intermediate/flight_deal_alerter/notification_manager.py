from twilio.rest import Client
from env.config import TW_ACCT as acct, TW_KEY as key, FROM_NUMBER, TO_NUMBER

class NotificationManager:

    def __init__(self):
        self.client = Client(acct, key)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)