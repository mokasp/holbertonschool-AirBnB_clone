#!/usr/bin/python3
""" File to test city """

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Class to test City """

    def test_city_state_id(self):
        """  Tests id data type """
        self.assertIsInstance(City().state_id, str)

    def test_city_state_id2(self):
        """  Tests id data type """
        self.assertIsNotNone(City().state_id)

    def test_city_name(self):
        """  Tests id data type """
        self.assertIsInstance(City().name, str)

    def test_city_name2(self):
        """  Tests id data type """
        self.assertIsNotNone(City().name)


if __name__ == "__main__":
    unittest.main()
