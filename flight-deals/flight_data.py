from datetime import datetime, timedelta


class FlightData:
    def __init__(self, fly_from: str, deal: dict,
                 date_from=(datetime.now() + timedelta(days=1)).now().date().strftime("%d/%m/%Y"),
                 date_to=(datetime.now() + timedelta(days=180)).date().strftime("%d/%m/%Y"),
                 currency="BRL", max_stop_overs=2):
        self.fly_from = fly_from
        self.fly_to = deal["iataCode"]
        self.date_from = date_from
        self.date_to = date_to
        self.price_to = deal["lowestPrice"]
        self.curr = currency
        if deal["maxStopovers"] == "-":
            self.max_stop_overs = max_stop_overs
        else:
            self.max_stop_overs = deal["maxStopovers"]
