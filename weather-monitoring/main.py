from models import session, WeatherData
from weather_data import get_weather
import datetime
from sqlalchemy import func

# Save weather data to the database
def save_weather_data():
    weather_data = get_weather()
    for city, data in weather_data.items():
        weather_entry = WeatherData(
            city=city,
            temperature=data['temp'],
            feels_like=data['feels_like'],
            weather_condition=data['weather'],
            timestamp=datetime.datetime.fromtimestamp(data['timestamp'])
        )
        session.add(weather_entry)
    session.commit()

# Generate daily summary
def daily_summary():
    result = session.query(
        WeatherData.city,
        func.avg(WeatherData.temperature).label('avg_temp'),
        func.max(WeatherData.temperature).label('max_temp'),
        func.min(WeatherData.temperature).label('min_temp'),
        WeatherData.weather_condition
    ).group_by(WeatherData.city).all()

    for city_data in result:
        print(f"City: {city_data.city}")
        print(f"Average Temp: {city_data.avg_temp:.2f}")
        print(f"Max Temp: {city_data.max_temp:.2f}")
        print(f"Min Temp: {city_data.min_temp:.2f}")
        print(f"Dominant Weather: {city_data.weather_condition}")

# Alert if temperature exceeds threshold for consecutive updates
def check_alerts():
    threshold_temp = 35  # Celsius
    consecutive_updates = 2
    weather_data = session.query(WeatherData).filter(WeatherData.temperature > threshold_temp).all()
    
    if len(weather_data) >= consecutive_updates:
        print(f"Alert: Temperature exceeded {threshold_temp}°C for {consecutive_updates} consecutive updates.")
