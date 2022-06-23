from twilio.rest import Client
from env.config import TW_ACCT as acct, TW_KEY as key, FROM_NUMBER, TO_NUMBER, CRED
import smtplib

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

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(CRED.hostname) as connection:
            connection.starttls()
            connection.login(CRED.username, CRED.password)
            for email in emails:
                connection.sendmail(
                    from_addr=CRED.username,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )