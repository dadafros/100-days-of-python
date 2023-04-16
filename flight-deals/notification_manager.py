import os
import smtplib
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
EMAIL_PASS = os.environ.get("EMAIL_PASS")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+15075965974",
            to="+5531920000682"
        )
        return message.sid

    def send_emails(self, users, subject: str, message: str):
        email = "louvor.oitavajovem@gmail.com"
        for user in users:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=EMAIL_PASS)
                connection.sendmail(from_addr=email,
                                    to_addrs=user['email'],
                                    msg=f"Subject:{subject}\n\nHi {user['firstName']} {user['lastName']}!\n{message}"
                                    .encode('utf-8'))
