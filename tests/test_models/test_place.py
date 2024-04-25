#!/usr/bin/python3
""" Test """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.new = Place(city_id="0001",
                            user_id="0001",
                            name="My_little_house",
                            description="My house is little",
                            number_rooms=1,
                            number_bathrooms=1,
                            max_guest=1,
                            price_by_night=1,
                            latitude=1.0,
                            longitude=1.0,
                            amenity_ids=[])

    def test_city_id(self):
        """ Test """
    
        self.assertEqual(type(self.new.city_id), str)

    def test_user_id(self):
        """ Test """

        self.assertEqual(type(self.new.user_id), str)

    def test_name(self):
        """ Test """
        self.assertEqual(type(self.new.name), str)

    def test_description(self):
        """ Test """

        self.assertEqual(type(self.new.description), str)

    def test_number_rooms(self):
        """ Test """
        self.assertEqual(type(self.new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test """
        self.assertEqual(type(self.new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test """

        self.assertEqual(type(self.new.max_guest), int)

    def test_price_by_night(self):
        """ Test """

        self.assertEqual(type(self.new.price_by_night), int)

    def test_latitude(self):
        """ Test """

        self.assertEqual(type(self.new.latitude), float)

    def test_longitude(self):
        """ Test """

        self.assertEqual(type(self.new.latitude), float)

    def test_amenity_ids(self):
        """ Test """

        self.assertEqual(type(self.new.amenity_ids), list)
