from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "BLR"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()


for city in sheet_data:
    destination = city["iataCode"]
    lowest_price = city["lowestPrice"]

    flight_price = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination
    )

    if flight_price and flight_price < lowest_price:
        message = f"""
        Low Price Alert!
        
        
        from = {ORIGIN_CITY_IATA}  
        to = {destination} 

        price: ₹{flight_price}

"""

        notification_manager.send_sms(message)


