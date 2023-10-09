#!/usr/bin/python3
""" File to test base_model.py """

import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Class to test BaseModel """

    def test_init(self):
        """  Tests id data type """
        self.assertIsInstance(BaseModel().id, str)

    def test_init1(self):
        """  Tests created_at data type """
        self.assertIsInstance(BaseModel().created_at, datetime.datetime)

    def test_init2(self):
        """  Tests updated_at data type """
        self.assertIsInstance(BaseModel().updated_at, datetime.datetime)

    def test_init3(self):
        """  Tests id data type """
        self.assertIsNotNone(BaseModel().id)

    def test_init4(self):
        """  Tests created_at data type """
        self.assertIsNotNone(BaseModel().created_at)

    def test_init5(self):
        """  Tests updated_at data type """
        self.assertIsNotNone(BaseModel().updated_at)
    
    def test_init6(self):
        """ Tests updated_at vs created_at """
        my_model = BaseModel()
        first_save = my_model.created_at
        my_model.save()
        first_update = my_model.updated_at
        self.assertNotEqual(first_save, first_update)

    def test_save(self):
        """ Tests created_at and updated_at are the same """
        my_model = BaseModel()
        first_update = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, first_update)

    def test_str(self):
        """ Tests the string representation of BaseModel """
        model = BaseModel()
        ID_Number = model.id
        strep = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        var = model.__str__()
        self.assertEqual(var, strep)
    """

    to_dict
    self.assertIsInstance - check for type

    str 
    self.assertEqual <--- This is the one I don't understand
    """