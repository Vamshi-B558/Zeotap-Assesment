-------To run and test the weather monitoring project, follow these step-by-step instructions-----------

---Step 1: Set Up Environment---

(1). Install Python and MySQL
Ensure you have Python 3.x installed. You can download it from here.
Install MySQL on your system if you don't have it. You can download it from here.

(2). Install Required Python Packages
Install the necessary Python libraries using pip (Python package installer). Run the following command in your terminal or command prompt:
pip install sqlalchemy requests schedule matplotlib pymysql mysqlclient

This command installs:
SQLAlchemy: For database operations.
Requests: For making API calls.
Schedule: For scheduling periodic tasks.
Matplotlib: For visualizations.
pymysql and mysqlclient: For MySQL interaction.

---Step 2: Set Up MySQL Database---

1. Create a New Database in MySQL
--Log in to MySQL:
--mysql -u root -p
--Create a database to store the weather data:
--CREATE DATABASE weather_db;
You can verify the creation with:
--SHOW DATABASES;

3. Set Up Database Credentials
Open the project file and configure the database connection (DB_CONFIG dictionary) with your MySQL credentials.
DB_CONFIG = {
    'user': 'root',
    'password': '18562', 
    'host': 'localhost',
    'database': 'weather_db',
}
Also, update the DATABASE_URI with your credentials:

DATABASE_URI = 'mysql+pymysql://root:your_password@localhost/weather_db'

---Step 3: Run Database Setup Script---

1. Create the Weather Data Table
To create the table in the MySQL database, ensure that the WeatherData model class is set up, as shown:

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String(50))
    temperature = Column(Float)
    feels_like = Column(Float)
    weather_condition = Column(String(50))
    timestamp = Column(DateTime, default=datetime.utcnow)

After the table class is defined, create the table in the database using SQLAlchemy:

Base.metadata.create_all(engine)

Run this script to create the table :python setup_database.py

This will create the weather_data table in the weather_db database.

---Step 4: Fetch and Store Weather Data---
1. API Key
Ensure that you have an API key from OpenWeatherMap. Replace the placeholder API key in the code with your actual key:

api_key = "'05e1bd7802d1eab18f5d36467fe02453"

2. Run the Weather Fetching Script
Now, run the script that fetches weather data from OpenWeatherMap and stores it in the database every 5 minutes:
->python main.py

The script will use the schedule library to fetch data for predefined cities every 5 minutes and store the data in your MySQL database.

---Step 5: Visualize Weather Data---
1. Fetch and Visualize Data
Once data is stored in the database, you can visualize the weather data for a particular city by running:
->python visualize.py

The script will prompt you to enter a city name, and it will display a bar chart showing the current temperature and "feels like" temperature using matplotlib.

---Step 6: Generate Daily Summary---

1. Run Daily Summary Script
To generate a daily summary of the weather data for all cities, run:
->python summary.py

This script queries the database to get average, maximum, and minimum temperatures for each city and prints the results.

---Step 7: Test Alerts---
1. Check for Temperature Alerts
The script can check if a city’s temperature exceeds a threshold for consecutive updates.

For example, in check_alerts(), the threshold is set to 35°C. If the temperature exceeds this value for consecutive updates, an alert will be triggered:

check_alerts()
Full Testing and Running Workflow
Set up MySQL database: Ensure your weather_db database is ready and the weather_data table is created.
--Run main.py: This fetches weather data every 5 minutes and stores it in the database.
--Run visualize.py: To visualize weather data for specific cities using bar charts.
--Run summary.py: To print daily weather summaries (average, max, min temperatures).
--Run check_alerts(): To monitor temperature alerts based on thresholds.
Commands Overview

Install Python dependencies:
->pip install sqlalchemy requests schedule matplotlib pymysql mysqlclient

->Create MySQL database:
->CREATE DATABASE weather_db;
Run table creation script:
->python setup_database.py

Run main weather fetching script:
->python main.py


Visualize city weather data:
-> python visualize.py

Generate daily summary:
->python summary.py

Check temperature alerts:
->python alerts.py
