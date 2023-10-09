#!/usr/bin/python3
""" File to test file_storage """
import unittest
import os
import datetime

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """ Class to test BaseModel """

    def setUp(self):
        """ Setting up """
        if os.path.exists('file.json'):
            os.remove("file.json")
        else:
            pass

    def tearDown(self):
        """ Tearing Down """
        pass

    def test_privateAttributes(self):
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            print(storage.objects)


if __name__ == 'main__':
    unittest.main()
