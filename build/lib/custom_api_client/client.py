import requests
from .exceptions import APIError


class WeatherAPIClient:
    """A client for interacting with the OpenWeatherMap API."""

    def __init__(self, api_key):
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.api_key = api_key

    def get_weather(self, city):
        """
        Fetch current weather data for a given city.

        Args:
            city (str): Name of the city.

        Returns:
            dict: Weather data as JSON.

        Raises:
            APIError: If the API request fails.
        """
        endpoint = f"{self.base_url}/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            raise APIError(f"Error fetching weather data: {response.text}")
        return response.json()

    def get_forecast(self, city):
        """
        Fetch weather forecast for a given city.

        Args:
            city (str): Name of the city.

        Returns:
            dict: Forecast data as JSON.

        Raises:
            APIError: If the API request fails.
        """
        endpoint = f"{self.base_url}/forecast"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            raise APIError(f"Error fetching forecast data: {response.text}")
        return response.json()
