import requests
import smtplib
import os

# Don't forget to export environment variables:
# export GMAIL_PASS=phyxbrvdjihehkca
# export OPENWEATHERMAP_APIKEY=a5e17ab40501733ee49df474587a7a21

API_KEY = os.environ.get("OPENWEATHERMAP_APIKEY")


def send_email(to_addr, subject, message):
    email = "louvor.oitavajovem@gmail.com"
    password = os.environ.get("GMAIL_PASS")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=to_addr,
                            msg=f"Subject:{subject}\n\n{message}")


def need_umbrella(forecast):
    for data in forecast:
        for weather in data["weather"]:
            if weather["id"] < 700:
                print("Bring Umbrella, sending email...")
                send_email("davi_bf@outlook.com", "Rain Alert", "Bring an umbrella!")
                return
    print("It's not going to rain")


# Get my location by IP
response = requests.get("http://ip-api.com/json/")
response.raise_for_status()
my_lat = response.json()["lat"]
my_lng = response.json()["lon"]

params = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": API_KEY,
    "units": "metric",
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
forecast_data = response.json()["list"][:4]  # Forecast for next 4 periods of 3 hours
need_umbrella(forecast_data)
