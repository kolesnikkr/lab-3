from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class Wind(Base):

    __tablename__ = "wind"

    id = Column(Integer, primary_key=True)

    wind_degree = Column(Integer)

    wind_kph = Column(Float)

    wind_direction = Column(String)

    should_go_outside = Column(Boolean)

    weather_id = Column(Integer, ForeignKey("weather.id"))

    weather = relationship("Weather")