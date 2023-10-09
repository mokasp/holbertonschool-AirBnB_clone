#!/usr/bin/python3
""" File to test file_storage """
import unittest
import os
import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """ Class to test FileStorage """

    def setUp(self):
        """ Setting up """
        if os.path.exists('file.json'):
            os.remove("file.json")
        else:
            pass

    def tearDown(self):
        """ Tearing Down """
        if os.path.exists('file.json'):
            os.remove("file.json")
        else:
            pass

    def test_privateObjects(self):
        """ test to check if __objects is truly private """
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            print(storage.__objects)

    def test_privateFile(self):
        """ tests to check if __file_path is truly private """
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            print(storage.__file_path)

    def test_all(self):
        """ tests to check if all method returns a dictionary """
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)


if __name__ == 'main__':
    unittest.main()
