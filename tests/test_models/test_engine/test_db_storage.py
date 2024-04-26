#!/usr/bin/python3
"""document document"""

from models.engine.db_storage import DBStorage
from models.state import State
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test is not relevant for DBStorage"
)
class test_DB_Storage(unittest.TestCase):
    """document document"""

    def test_documentation(self):
        """document document"""
        self.assertIsNot(DBStorage.__doc__, None)

    def test_get(self):
        all = DBStorage().all(State)
        special = all["State.028d6999-d4ff-4932-8a53-940633786b88"]
        self.assertEquals(special, DBStorage().get(State, "028d6999-d4ff-4932-8a53-940633786b88"))

    def test_count(self):
        all = DBStorage().all()
        len = len(all)
        self.assertEquals(len, DBStorage().get())
