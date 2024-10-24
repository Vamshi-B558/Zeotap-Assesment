import schedule
import time
from main import save_weather_data

# Schedule data fetching every 5 minutes
schedule.every(5).minutes.do(save_weather_data)

while True:
    schedule.run_pending()
    time.sleep(1)
