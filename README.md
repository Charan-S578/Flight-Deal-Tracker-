# Flight Deal Tracker ✈️

## Overview

Flight Deal Tracker is a Python automation project that monitors flight prices and sends alerts when ticket prices drop below a predefined threshold. The application reads destination data from a Google Sheet using the Sheety API, searches for flight prices using the SerpAPI Google Flights API, and notifies users when a cheaper flight is found.

## Features

* Read destination cities and price thresholds from Google Sheets.
* Automatically fetch airport IATA codes.
* Search for the cheapest flights from tomorrow up to 6 months ahead.
* Compare current flight prices against target prices.
* Send instant SMS notifications when deals are found.
* Easily configurable origin airport and destinations.

## Project Structure

```text
flight-deals/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── notification_manager.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python 3
* Sheety API
* SerpAPI Google Flights API
* Twilio SMS API (for notifications)
* Requests Library

## How It Works

1. Retrieve destination data from Google Sheets.
2. Read destination airport IATA codes and target prices.
3. Search available flights from the origin airport.
4. Compare live flight prices with stored lowest prices.
5. Send an SMS alert if a cheaper flight is discovered.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/flight-deal-tracker.git
cd flight-deal-tracker
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

```env
SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_TOKEN=your_sheety_token
SERPAPI_API_KEY=your_serpapi_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

4. Run the application:

```bash
python main.py
```

## Example Alert

```text
Low Price Alert!

From: BLR
To: CDG

Price: ₹24,999
```

## Future Enhancements

* Email notifications
* Multiple origin airports
* Web dashboard
* Historical price tracking
* Scheduled automated checks using cron jobs or cloud functions

## License

This project is open-source and available under the MIT License.

