#!/usr/bin/python3
""" File to test file_storage """
import unittest
import os
import json
import datetime

from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Class to test FileStorage """

    def setUp(self):
        """ Setting up """
        if os.path.exists("file.json"):
            os.remove("file.json")
        else:
            with open("file.json", "x"):
                pass

    def tearDown(self):
        """ Tearing Down """
        if os.path.exists("file.json"):
            os.remove("file.json")
        else:
            pass

    def test_privateObjects(self):
        """ test to check if __objects is truly private """
        items = FileStorage()
        with self.assertRaises(AttributeError):
            if type(items.__objects) is str:
                pass

    def test_privateFile(self):
        """ tests to check if __file_path is truly private """
        stuff = FileStorage()
        with self.assertRaises(AttributeError):
            if type(stuff.__file_path) is str:
                pass

    def test_all(self):
        """ tests to check if all method returns a dictionary """
        thing = FileStorage()
        self.assertIsInstance(thing.all(), dict)

    def test_basemodelnew(self):
        """ test for new method """
        new_storage = FileStorage()
        old = new_storage.all()
        BaseModel()
        new_storage.save()
        new = new_storage.all()
        self.assertNotEqual(new, old)

    def test_filestoragenew(self):
        """ test that direct call to new works """
        obj = BaseModel()
        new_storage = FileStorage()
        new_storage.__objects = {}
        old = new_storage.__objects
        new_storage.new(obj)
        self.assertNotEqual(new_storage.all(), old)

    def test_reload(self):
        """ test for reload method"""
        reload_storage_1 = FileStorage()
        old = reload_storage_1.all()
        BaseModel()
        reload_storage_1.save()
        reload_storage_2 = FileStorage()
        reload_storage_2.reload()
        new = reload_storage_2.all()
        self.assertNotEqual(new, old)

    def test_destroythis(self):
        """ test to check destroy helper method """
        new_storage = FileStorage()
        obj = BaseModel()
        key = f"BaseModel.{obj.id}"
        old = new_storage.all()
        new_storage.destroy_this(key)
        new = new_storage.all()
        self.assertNotEqual(new, old)

    def test_save(self):
        save_storage = FileStorage()
        if os.path.exists("file.json"):
            os.remove("file.json")
        BaseModel()
        save_storage.save()
        self.assertEqual(os.path.exists("file.json"), True)


if __name__ == "__main__":
    unittest.main()
