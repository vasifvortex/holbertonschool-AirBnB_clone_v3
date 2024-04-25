#!/usr/bin/python3
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
