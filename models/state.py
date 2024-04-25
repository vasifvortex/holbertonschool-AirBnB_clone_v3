#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete",
                          backref=backref("state", cascade="all, delete"))

    @property
    def cities(self):
        from models import storage
        """Getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id"""
        city_instances = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
