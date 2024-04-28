#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from os import getenv, remove, path
from models.state import State
from models.city import City


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "DBStorage")
class test_fileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            remove("file.json")
        except Exception:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        length_before = len(list(storage.all().values()))
        new = BaseModel()
        new.save()
        length_after = len(list(storage.all().values()))
        self.assertTrue(length_after - 1 == length_before)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(path.exists("file.json"))

    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(path.getsize("file.json"), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(path.exists("file.json"))

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(path.exists("file.json"))

    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        new.save()
        _id = new.to_dict()["id"]
        temp = list(storage.all().keys())[0]
        self.assertEqual(temp, "BaseModel" + "." + _id)

    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage

        self.assertEqual(type(storage), FileStorage)

    def test_get_cls(self):
        """Test for get() method of DBsStorage"""
        state = State()
        state.save()
        state_id = state.id
        obj = storage.get(State, state_id)
        obj2 = storage.get(State, 123)
        self.assertEqual(state, obj)
        self.assertNotEqual(obj, obj2)

    def test_count(self):
        """Test for count() method of DBsStorage"""
        state = State()
        state.save()
        city = City()

        city.save()
        states = storage.count(State)
        all_objs = storage.count()
        self.assertEqual(states, 1)
        self.assertTrue(states < all_objs)
