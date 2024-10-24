import datetime
from turtle import pd
import requests
from sqlalchemy import Engine, text  # Make sure to import text

def fetch_weather_data(city):
    api_key = "e7604470d76e51694dde69a1b73c2f54"  # Your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Parse relevant data
        return {
            'city': data.get('name'),
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'weather_condition': data['weather'][0]['description'],
            'timestamp': datetime.fromtimestamp(data['dt'])  # Convert UNIX timestamp to datetime
        }
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return None





