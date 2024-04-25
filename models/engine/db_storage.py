#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Creates a new FileStorage instance"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for cls in classes:
                objects += self.__session.query(cls).all()

        result = {}
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result[key] = obj

        return result

    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """Saves storage to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from storage"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage from file"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.close()
        return self.__session
