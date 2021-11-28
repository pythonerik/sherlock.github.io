from twilio.rest import Client
import smtplib

TWILIO_SID = "ACaae3e00d23dbc4d225523c8fcf28cb8d"
TWILIO_AUTH_TOKEN = "6984c9a5f0ab9ed2043db27b943a3323"
TWILIO_VIRTUAL_NUMBER = "+19388883833"
TWILIO_VERIFIED_NUMBER = "+14153421282"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "pythonerik@gmail.com"
MY_PASSWORD = "id4id4098"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )