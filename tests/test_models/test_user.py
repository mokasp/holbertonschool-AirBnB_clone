#!/usr/bin/python3
""" File to test user """

import unittest
from models.user import User


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


if __name__ == "__main__":
    unittest.main()
