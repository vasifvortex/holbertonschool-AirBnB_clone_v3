#!/usr/bin/python3
""" Module for testing DB storage """
from os import getenv
import unittest
from models.base_model import BaseModel
from models import storage
from models.state import State


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "DBStorage")
class TestDBStorage(unittest.TestCase):
    """ Class to test the database storage method """

    def test_all(self):
        """ Test for all() method of DBsStorage """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_get_cls(self):
        """ Test for get() method of DBsStorage """
        state = State(name="Baku")
        state.save()
        state_id = state.id
        obj = storage.get(State, state_id)
        obj2 = storage.get(State, 123)
        self.assertEqual(state, obj)
        self.assertFalse(obj is obj2)

    def test_count(self):
        """ Test for count() method of DBsStorage """
        count = storage.count()
        state = State(name="Baku")
        state.save()
        new_count = storage.count()
        self.assertTrue(new_count == count + 1)
        state2 = State(name="Ganja")
        state2.save()
        new_count = storage.count()
        self.assertTrue(new_count == count + 2)
        storage.delete(state)
        new_count = storage.count()
        self.assertTrue(new_count == count + 1)
        storage.delete(state2)
        new_count = storage.count()
        self.assertTrue(new_count == count)
