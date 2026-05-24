from app.database import SessionLocal
from app.models.weather import Weather
from app.models.wind import Wind

session = SessionLocal()
country_name = input("Enter country: ")
results = session.query(Weather, Wind).join(
    Wind,
    Weather.id == Wind.weather_id).filter(
    Weather.country == country_name).all()

for weather, wind in results:
    print("Country:", weather.country)
    print("Temperature:", weather.temperature)
    print("Wind kph:", wind.wind_kph)
    print("Should go outside:", wind.should_go_outside)
    print("----------------")