#!/usr/bin/python3
""" File to test user, state, city, place, amenity, and review """

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestUser(unittest.TestCase):
    """ Class to test User """

    def test_user_email(self):
        """  Tests data type """
        self.assertIsInstance(User().email, str)

    def test_user_email2(self):
        """  Tests is not none"""
        self.assertIsNotNone(User().email)

    def test_user_password(self):
        """  Tests data type """
        self.assertIsInstance(User().password, str)

    def test_user_password2(self):
        """  Tests is not none"""
        self.assertIsNotNone(User().password)

    def test_user_first_name(self):
        """  Tests data type """
        self.assertIsInstance(User().first_name, str)

    def test_user_first_name2(self):
        """  Tests is not none"""
        self.assertIsNotNone(User().first_name)

    def test_user_last_name(self):
        """  Tests data type """
        self.assertIsInstance(User().last_name, str)

    def test_user_last_name2(self):
        """  Tests is not none"""
        self.assertIsNotNone(User().last_name)


class TestState(unittest.TestCase):
    """ Class to test State """

    def test_state_name(self):
        """  Tests id data type """
        self.assertIsInstance(State().name, str)

    def test_state_name2(self):
        """  Tests id data type """
        self.assertIsNotNone(State().name)


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


class TestAmenity(unittest.TestCase):
    """ Class to test Amenity """

    def test_amenity_name(self):
        """  Tests id data type """
        self.assertIsInstance(Amenity().name, str)

    def test_amenity_name2(self):
        """  Tests id data type """
        self.assertIsNotNone(Amenity().name)


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


class TestReview(unittest.TestCase):
    """ Class to test Review """

    def test_review(self):
        """  Tests data type """
        self.assertIsInstance(Review().place_id, str)
        self.assertIsInstance(Review().user_id, str)
        self.assertIsInstance(Review().text, str)

    def test_review2(self):
        """  Tests for is not None """
        self.assertIsNotNone(Review().place_id)
        self.assertIsNotNone(Review().user_id)
        self.assertIsNotNone(Review().text)


if __name__ == "__main__":
    unittest.main()
