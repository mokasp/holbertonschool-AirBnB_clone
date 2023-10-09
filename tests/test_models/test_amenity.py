#!/usr/bin/python3
""" File to test Amenity """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Class to test Amenity """

    def test_amenity_name(self):
        """  Tests id data type """
        self.assertIsInstance(Amenity().name, str)

    def test_amenity_name2(self):
        """  Tests id data type """
        self.assertIsNotNone(Amenity().name)


if __name__ == "__main__":
    unittest.main()
