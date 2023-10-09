#!/usr/bin/python3
""" File to test file_storage """
import unittest
import os
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
            print(items.__objects)

    def test_privateFile(self):
        """ tests to check if __file_path is truly private """
        stuff = FileStorage()
        with self.assertRaises(AttributeError):
            print(stuff.__file_path)

    def test_all(self):
        """ tests to check if all method returns a dictionary """
        thing = FileStorage()
        self.assertIsInstance(thing.all(), dict)

    def test_new(self):
        """ test for new method """
        new_storage = FileStorage()
        old = new_storage.all()
        BaseModel()
        new_storage.save()
        new = new_storage.all()
        self.assertNotEqual(new, old)

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

    def test_save(self):
        """ tests save method """
        save_storage = FileStorage()
        old = save_storage.all()
        BaseModel()
        save_storage.save()
        new = save_storage.all()
        self.assertNotEqual(new, old)


if __name__ == 'main__':
    unittest.main()
