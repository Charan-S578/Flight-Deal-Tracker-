import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

class DataManager:
    def get_destination_data(self):
        #This class is responsible for talking to the google sheet.
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)

        data = response.json()
        print(data)
        return data["sheet1"]
