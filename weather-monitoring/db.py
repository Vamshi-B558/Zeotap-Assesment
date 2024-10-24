from sqlalchemy import create_engine, Table, Column, Integer, String, Float, DateTime, MetaData
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database connection setup
DATABASE_URI = 'mysql+pymysql://username:password@localhost/weather_db'  # Update with your credentials
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def store_weather_data(data):
    # Define the table structure
    metadata = MetaData()
    weather_data = Table('weather_data', metadata,
        Column('id', Integer, primary_key=True),
        Column('city', String(255)),
        Column('temperature', Float),
        Column('feels_like', Float),
        Column('weather_condition', String(255)),
        Column('timestamp', DateTime)
    )
    
    # Insert data into the database
    insert_stmt = weather_data.insert().values(
        city=data['city'],
        temperature=data['temperature'],
        feels_like=data['feels_like'],
        weather_condition=data['weather_condition'],
        timestamp=data['timestamp']
    )

    try:
        session.execute(insert_stmt)
        session.commit()  # Commit the transaction
        print("Data stored successfully.")
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
        session.rollback()  # Rollback in case of error
    finally:
        session.close()  # Close the session
