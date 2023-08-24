#!/usr/bin/python3
""" 0xBOOM! """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from .place import place_amenity


class Amenity(BaseModel, Base):
    """ Def to table `amenities
    Attributes:
        name association to `Place`
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
