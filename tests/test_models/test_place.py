#!/usr/bin/python3
""" File to test place """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Class to test Place """

    def test_place(self):
        """  Tests data type """
        self.assertIsInstance(Place().city_id, str)
        self.assertIsInstance(Place().user_id, str)
        self.assertIsInstance(Place().name, str)
        self.assertIsInstance(Place().description, str)
        self.assertIsInstance(Place().number_rooms, int)
        self.assertIsInstance(Place().number_bathrooms, int)
        self.assertIsInstance(Place().max_guest, int)
        self.assertIsInstance(Place().price_by_night, int)
        self.assertIsInstance(Place().latitude, float)
        self.assertIsInstance(Place().longitude, float)
        self.assertIsInstance(Place().amenity_ids, list)

    def test_place2(self):
        """  Tests for is not none """
        self.assertIsNotNone(Place().city_id)
        self.assertIsNotNone(Place().user_id)
        self.assertIsNotNone(Place().name)
        self.assertIsNotNone(Place().description)
        self.assertIsNotNone(Place().number_rooms)
        self.assertIsNotNone(Place().number_bathrooms)
        self.assertIsNotNone(Place().max_guest)
        self.assertIsNotNone(Place().price_by_night)
        self.assertIsNotNone(Place().latitude)
        self.assertIsNotNone(Place().longitude)
        self.assertIsNotNone(Place().amenity_ids)


if __name__ == "__main__":
    unittest.main()
