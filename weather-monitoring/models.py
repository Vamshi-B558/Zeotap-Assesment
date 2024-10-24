from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from config import DB_CONFIG

# Create the connection string for MySQL
engine = create_engine(f"mysql+mysqldb://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}")
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    city = Column(String(50))
    temperature = Column(Float)
    feels_like = Column(Float)
    weather_condition = Column(String(50))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create the tables in the database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
