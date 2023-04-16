import os
import requests
from pprint import pprint

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/78ea250cebb814128750091852f45ff4/flightDeals"


class DataManager:
    def __init__(self):
        self.response = requests.get(SHEETY_ENDPOINT + "/prices", headers={"Authorization": SHEETY_TOKEN})
        self.response.raise_for_status()
        self.data = {"prices": self.response.json()["prices"]}
        self.response = requests.get(SHEETY_ENDPOINT + "/users", headers={"Authorization": SHEETY_TOKEN})
        self.response.raise_for_status()
        self.data.update({"users": self.response.json()["users"]})

    def update_row(self, index, iata_code):
        json = {
            "price": {
                "iataCode": iata_code,
            }
        }
        response = requests.put(SHEETY_ENDPOINT + f"/{index}", headers={"Authorization": SHEETY_TOKEN}, json=json)
        response.raise_for_status()
        return response.text

    def get_data(self, sheet: str):
        return self.data[sheet]
