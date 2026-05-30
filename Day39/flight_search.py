import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


class FlightSearch:
    def search_flights(self, origin, destination):
        #This is class responsible for talking to the flight search API.
        tomorrow = datetime.now() + timedelta(days=1)
        six_months = datetime.now() + timedelta(days=180)

        params = {
            "engine": "google_flights",
            "departure_id": "origin",
            "arrival_id": "destination",
            "outbound_date": "tomorrow.strftime('Y%m%d%')",
            "return_date": "six_months.strftime('Y%m%d%)",
            "currency": "INR",
            "hl": "en",
            "api_key": SERPAPI_KEY
        }

        response = requests.get( "https://serpapi.com/search.json", params=params)

        data = response.json()

        try:
            price = data["best_flights"][0]["price"]
            return price
        except:
            return None