import requests
import os
from twilio.rest import Client

# API KEYS ARE STORED IN ENVIRONMENT VARIABLES, SEE PYCHARM RUN CONFIGURATION
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": os.environ["STOCK_API_KEY"],
}
response = requests.get("https://www.alphavantage.co/query", params=params)
response.raise_for_status()
stock_data = response.json()
last_refreshed = stock_data["Meta Data"]["3. Last Refreshed"]
opening_price = float(stock_data["Time Series (Daily)"][last_refreshed]["1. open"])
closing_price = float(stock_data["Time Series (Daily)"][last_refreshed]["5. adjusted close"])
variation = (closing_price - opening_price) / opening_price * 100

if abs(variation) >= 1:
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    params = {
        "q": f"{COMPANY_NAME} OR {STOCK}",
        "searchIn": "title",
        "apikey": os.environ["NEWS_API_KEY"],
    }
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    response.raise_for_status()
    articles = response.json()["articles"][:3]
    print(articles)

    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    for article in articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: {variation:.2f}%\nHeadline: {article['title']}\nBrief: {article['description']}",
            from_='+15075965974',
            to='+5531920000682'
        )
        print(message.sid)
else:
    print(f"{STOCK} price is calm")
