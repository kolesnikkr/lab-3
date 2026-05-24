from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from app.database import Base


class Weather(Base):

    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)

    country = Column(String)

    temperature = Column(Float)

    last_updated = Column(DateTime)