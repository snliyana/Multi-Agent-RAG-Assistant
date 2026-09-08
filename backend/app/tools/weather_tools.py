import os
import requests

from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "OPENWEATHER_API_KEY is not configured."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(
        url,
        params=params,
        timeout=10,
    )

    if response.status_code != 200:
        return f"Unable to retrieve weather data for {city}."

    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    return (
        f"City: {city}\n"
        f"Temperature: {temperature}°C\n"
        f"Feels like: {feels_like}°C\n"
        f"Humidity: {humidity}%\n"
        f"Condition: {condition}"
    )