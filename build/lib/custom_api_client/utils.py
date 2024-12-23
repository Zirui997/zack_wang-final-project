def parse_weather_data(data):
    """
    Parse and format weather data for easier interpretation.

    Args:
        data (dict): Raw weather data from the API.

    Returns:
        dict: Parsed weather data.
    """
    return {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }
