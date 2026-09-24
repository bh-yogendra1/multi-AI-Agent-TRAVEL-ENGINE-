import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(query):
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        flights = []

        if "data" in data and data["data"]:
            for flight in data["data"][:5]:
                airline = flight.get("airline", {}).get("name", "Unknown")
                departure = flight.get("departure", {}).get("airport", "Unknown")
                arrival = flight.get("arrival", {}).get("airport", "Unknown")
                status = flight.get("flight_status", "Unknown")

                flights.append(
                    f"Airline: {airline}\nDeparture: {departure}\nArrival: {arrival}\nStatus: {status}\n"
                )
            return "\n".join(flights)
        else:
            return "No flight data found or API limit reached."
    except Exception as e:
        return f"Error fetching flights: {str(e)}"