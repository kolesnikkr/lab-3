import pandas as pd

from app.database import SessionLocal
from app.models.weather import Weather
from app.models.wind import Wind

session = SessionLocal()

df = pd.read_csv("weather.csv", low_memory=False)

df = df.head(1000)

for index, row in df.iterrows():

    print(f"Processing row {index}")

    weather = Weather(
        country=str(row["country"]),
        temperature=float(row["temperature_celsius"]),
        last_updated=pd.to_datetime(row["last_updated"])
    )

    session.add(weather)

    session.commit()

    should_go = float(row["wind_kph"]) < 20

    wind = Wind(
        wind_degree=int(float(row["wind_degree"])),
        wind_kph=float(row["wind_kph"]),
        wind_direction=str(row["wind_direction"]),
        should_go_outside=should_go,
        weather_id=weather.id
    )

    session.add(wind)

    session.commit()

print("CSV imported")