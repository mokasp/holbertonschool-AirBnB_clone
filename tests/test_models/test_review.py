#!/usr/bin/python3
""" File to test review """

import unittest
from models.review import Review


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
