#!/usr/bin/python3
""" File to test State """

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Class to test State """

    def test_state_name(self):
        """  Tests id data type """
        self.assertIsInstance(State().name, str)

    def test_state_name2(self):
        """  Tests id data type """
        self.assertIsNotNone(State().name)


if __name__ == "__main__":
    unittest.main()
