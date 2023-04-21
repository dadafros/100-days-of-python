from bs4 import BeautifulSoup
import requests
import smtplib
import os
# import lxml # another parser

AMAZON_PRODUCT_URL = input("Paste an Amazon product link to monitor price:\n")


def send_email(to_addr, subject, message):
    email = "louvor.oitavajovem@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=os.environ.get("GMAIL_PASS"))
        connection.sendmail(from_addr=email,
                            to_addrs=to_addr,
                            msg=f"Subject:{subject}\n\n{message}".encode("utf-8"))


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;"
              "q=0.8,application/signed-exchange;v=b3;q=0.7",
    "upgrade-insecure-requests": "1",
}
response = requests.get(AMAZON_PRODUCT_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find("span", id="productTitle").getText().strip()
currency = soup.find("span", class_="a-price-symbol").getText()
price = soup.find("span", class_="a-price-whole").getText() + soup.find("span", class_="a-price-fraction").getText()
price = price.replace(".", "")
price = float(price.replace(",", "."))

target = float(input("What is the price target? "))
user_email = input("What is your email? ")

if price <= target:
    print("Sending email! Content:")
    msg = f"Your {title} has reached your price target and its cost is {currency}{price}!\n" + AMAZON_PRODUCT_URL
    print(msg)
    send_email(user_email, "Price Alert", msg)
else:
    print("Not your lucky day.")
