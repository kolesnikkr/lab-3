from app.database import SessionLocal
from app.models.weather import Weather

session = SessionLocal()

country_name = input("Enter country: ")

results = session.query(Weather).filter(
    Weather.country == country_name
).all()

for weather in results:

    print("Country:", weather.country)
    print("Temperature:", weather.temperature)
    print("Updated:", weather.last_updated)
    print("-------------------")