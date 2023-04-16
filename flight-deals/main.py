from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch, search_iata_code
from notification_manager import NotificationManager

fly_from = search_iata_code(input("Where are you flying from? "))

data_manager = DataManager()
deals = data_manager.get_data("prices")
for deal in deals:
    if deal["iataCode"] == "":
        deal["iataCode"] = search_iata_code(deal["city"])
        data_manager.update_row(deal["id"], deal["iataCode"])

flights = []
for deal in deals:
    flights.append(FlightData(fly_from, deal))

notification = NotificationManager()
for flight in flights:
    result = FlightSearch(flight).search_flight()
    print(result)
    if result:
        stopovers = len(result['route']) - 2
        via_city = []
        for route in result['route']:
            if route['cityTo'] != result['cityTo'] and route['cityTo'] != result['cityFrom']:
                via_city.append(route['cityTo'])

        message = f"Low price alert! Only {result['price']} {flight.curr} to fly from "\
                  f"{result['cityFrom']}-{result['flyFrom']} to {result['cityTo']}-{result['flyTo']}. "\
                  f"Departure: {result['route'][0]['local_departure'].split('T')[0]} "\
                  f"Arrival: {result['route'][-1]['local_arrival'].split('T')[0]}. "
        stop_message = f"Flight has {stopovers} total stop overs, via {'/'.join(via_city)}. "
        link = f"Link: {result['deep_link']}"

        users = data_manager.get_data("users")
        if stopovers:
            notification.send_emails(users, "New Flight Deal!", message + stop_message + link)
            # notification.send_sms(message + stop_message + link)
        else:
            notification.send_emails(users, "New Flight Deal!", message + link)
            # notification.send_sms(message + link)
