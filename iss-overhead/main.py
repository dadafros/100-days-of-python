import os

import requests
from datetime import datetime, timezone, timedelta
import smtplib
import os


def send_email(to_addr, subject, message):
    email = "louvor.oitavajovem@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=os.environ.get("GMAIL_PASS"))
        connection.sendmail(from_addr=email,
                            to_addrs=to_addr,
                            msg=f"Subject:{subject}\n\n{message}")


# Get my location by IP
response = requests.get("http://ip-api.com/json/")
response.raise_for_status()
my_lat = response.json()["lat"]
my_lng = response.json()["lon"]
params = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}
print("Your location: ", my_lat, my_lng)

# Get sunrise and sunset times for my location
response = requests.get("https://api.sunrise-sunset.org/json", params)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

# Get ISS location
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_longitude = float(response.json()["iss_position"]["longitude"])
iss_latitude = float(response.json()["iss_position"]["latitude"])
print("ISS location: ", iss_latitude, iss_longitude)

# Get current time
time_now = str(datetime.now(timezone.utc))
print("Sunrise: " + sunrise)
print("Sunset: " + sunset)
print("Now: " + time_now)

if datetime.fromisoformat(sunset).time() <= datetime.fromisoformat(time_now).time() <= datetime.fromisoformat(sunrise).time():
    print("It's dark, let's see if ISS is nearby...")
    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_lng - 5 <= iss_longitude <= my_lng + 5:
        print("You can see the ISS! Sending email notification...")
        send_email("davi_bf@outlook.com", "ISS is in your area", "Look up!")
