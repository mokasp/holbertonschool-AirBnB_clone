#!/usr/bin/python3
""" File to test base_model.py """

import unittest
import os
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Class to test BaseModel """

    def setUp(self):
        """ Setting up """
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """ Tearing Down """
        del self.model
        os.remove("file.json")

    def test_init(self):
        """  Tests id data type """
        var = BaseModel()
        self.assertIsInstance(var.id, str)

    def test_init1(self):
        """  Tests created_at data type """
        var = BaseModel()
        self.assertIsInstance(var.created_at, datetime.datetime)

    def test_init2(self):
        """  Tests updated_at data type """
        var = BaseModel()
        self.assertIsInstance(var.updated_at, datetime.datetime)

    """self.assertIsNotNone - check for none
    self.assertIsInstance - check for type
    self.assertEqual - in the init (almost?)

    save
    self.assertNotEqual - save

    to_dict
    self.assertIsInstance - check for type

    str 
    self.assertEqual <--- This is the one I don't understand
    """