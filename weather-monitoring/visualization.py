import requests
import matplotlib.pyplot as plt

def fetch_weather_data(city):
    api_key = "05e1bd7802d1eab18f5d36467fe02453"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
          
            city_name = data.get('name')
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            weather_condition = data['weather'][0]['description']
            timestamp = data['dt'] 

            print(f"City: {city_name}, Temperature: {temperature}°C, Feels Like: {feels_like}°C, Weather: {weather_condition}")
            return {
                'city': city_name,
                'temperature': temperature,
                'feels_like': feels_like,
                'weather_condition': weather_condition,
                'timestamp': timestamp
            }
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def visualize_weather_data(city_data):
    if city_data:
        # Data to visualize
        labels = ['Temperature', 'Feels Like']
        values = [city_data['temperature'], city_data['feels_like']]

        # Create a bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'orange'])
        plt.title(f"Weather Data for {city_data['city']}")
        plt.ylabel("Temperature (°C)")
        plt.ylim(0, max(values) + 5)
        plt.grid(axis='y')

      
        plt.show()


city_name = input("Enter the name of the city: ")  
city_data = fetch_weather_data(city_name)
visualize_weather_data(city_data)  
