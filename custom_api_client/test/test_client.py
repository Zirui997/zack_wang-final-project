import pytest
from unittest.mock import patch
from custom_api_client.client import WeatherAPIClient
from custom_api_client.exceptions import APIError


@pytest.fixture
def client():
    return WeatherAPIClient(api_key="3d46ec00681adc394a632feaf95f8af9")


def test_get_weather(client):
    mock_response = {
        "name": "London",
        "main": {"temp": 15.0, "humidity": 80},
        "weather": [{"description": "clear sky"}],
        "wind": {"speed": 5.0},
    }
    with patch("requests.get", return_value=MockResponse(mock_response, 200)):
        result = client.get_weather("London")
        assert result["name"] == "London"
        assert result["main"]["temp"] == 15.0


def test_get_weather_error(client):
    with patch("requests.get", return_value=MockResponse({"message": "city not found"}, 404)):
        with pytest.raises(APIError):
            client.get_weather("InvalidCity")


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = str(json_data) 

    def json(self):
        return self.json_data
