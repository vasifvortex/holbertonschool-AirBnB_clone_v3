#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               cascade="all, delete", backref="place")
    else:
        @property
        def reviews(self):
            from models import storage
            """Getter attribute reviews that returns
            the list of Review instances with place_id
            equals to the current Place.id"""
            review_instances = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_instances.append(review)
            return review_instances
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def amenities(self):
            from models.amenity import Amenity
            from models import storage
            """Getter attribute amenities that
              returns the list of Amenity instances"""
            amenity_instances = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_instances.append(amenity)
            return amenity_instances

        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            """Setter attribute amenities that handles append method
              for adding an Amenity.id to the attribute amenity_ids"""

            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
            else:
                pass
