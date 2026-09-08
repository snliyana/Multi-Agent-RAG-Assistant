from dotenv import load_dotenv

load_dotenv()

from backend.app.tools.weather_tools import get_weather


result = get_weather.invoke(
    {
        "city": "Kuala Lumpur"
    }
)

print(result)