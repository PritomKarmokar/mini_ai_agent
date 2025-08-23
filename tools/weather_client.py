import requests

from confg import loadenv

WEATHER_BASE_URL = loadenv.WEATHER_INFO_URL
GEOCODE_BASE_URL = loadenv.GEOCODE_FETCH_URL

class WeatherClient:
    @staticmethod
    def geocode_city(city: str):
        url = f"{GEOCODE_BASE_URL}/search?name={city}&count=1"
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            print(data)
            results = data.get("results")
            if not results:
                return None, f"City not found: {city}"

            place = results[0]
            return (place["latitude"], place["longitude"]), None
        except Exception as e:
            return None, str(e)

    def fetch_weather(self, city: str) -> str:
        print("city:", city)
        co_ordinates, err = self.geocode_city(city)
        if err:
            return f"Geocoding error: {err}"
        if not co_ordinates:
            return f"Could not find {city}"

        lat, lon = co_ordinates
        url = f"{WEATHER_BASE_URL}?latitude={lat}&longitude={lon}&current_weather=true"

        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            temp = data["current_weather"]["temperature"]
            return f"{city.title()}: {temp} °C"
        except Exception as e:
            return f"Weather API error: {e}"

weather_client = WeatherClient()

