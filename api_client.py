import json
import requests, os

from dotenv import load_dotenv
load_dotenv()

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def _get_api_key():
    """Fetch the API key from your configuration file.

    Expects a configuration file named ".env" with structure:

    """
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    return WEATHER_API_KEY


def build_weather_query(city_input, measurement_unit):
    """Builds the URL for an API request to OpenWeather's weather API.

    Args:
        city_input (List[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature

    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint
    """
    api_key = _get_api_key()

    # units = "imperial" if imperial else "metric"
    url = f"{BASE_WEATHER_API_URL}?q={city_input}&units={measurement_unit}&appid={api_key}"

    return url


def get_weather_data(query_url):
    """Makes an API request to a URL and returns the data as a Python object.

    Args:
        query_url (str): URL formatted for OpenWeather's city name endpoint

    Returns:
        dict: Weather information for a specific city
    """

    response = requests.get(query_url)
    data = json.loads(response.text)
    
    return {"main": data["main"], "weather": data["weather"][0]}