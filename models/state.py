#!/usr/bin/python3
""" 0d Cities """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .city import City
from .base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """Des:
        name o-many-association to `City`
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Gettde.
            """
            from . import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
