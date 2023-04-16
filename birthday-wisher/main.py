import smtplib
from datetime import datetime
import random
import pandas as pd


def send_email(to_addr, subject, message):
    email = "dadafrossard@gmail.com"
    password = "mkrskrzwiiaxqxtz"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=to_addr,
                            msg=f"Subject:{subject}\n\n{message}")


now = datetime.now()
birthdays = pd.read_csv("birthdays.csv").to_dict("records")
for birthday in birthdays:
    if birthday["day"] == now.day and birthday["month"] == now.month:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read().replace("[NAME]", birthday["name"])
        with open("quotes.txt") as file:
            quote = random.choice(file.read().split("\n"))
        send_email(birthday["email"], "Happy Birthday!", letter + "\n\n" + quote)
