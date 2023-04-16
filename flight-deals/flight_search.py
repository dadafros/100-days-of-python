import os
import requests
from flight_data import FlightData

TEQUILA_KIWI_API_KEY = os.environ.get("TEQUILA_KIWI_API_KEY")


def search_iata_code(city):
    params = {
        "term": city,
        "location_types": "city",
    }
    response = requests.get("https://api.tequila.kiwi.com/locations/query",
                            headers={"apikey": TEQUILA_KIWI_API_KEY}, params=params)
    response.raise_for_status()
    return response.json()["locations"][0]["code"]


class FlightSearch:
    def __init__(self, flight_data: FlightData):
        self.flight_data = flight_data

    def search_flight(self):
        params = {
            "fly_from": self.flight_data.fly_from,
            "fly_to": self.flight_data.fly_to,
            "date_from": self.flight_data.date_from,
            "date_to": self.flight_data.date_to,
            "price_to": self.flight_data.price_to,
            "curr": self.flight_data.curr,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": self.flight_data.max_stop_overs,
        }
        response = requests.get("https://api.tequila.kiwi.com/v2/search",
                                headers={"apikey": TEQUILA_KIWI_API_KEY}, params=params)
        response.raise_for_status()
        try:
            return response.json()["data"][0]
        except IndexError:
            return None
