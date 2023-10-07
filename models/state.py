#!/usr/bin/python3
""" Module containing the class State """
# Michael 1:38 PM 10/7
from models.base_model import BaseModel


class State(BaseModel):
    """
    A class called State with a public attribute
    for the name of the state.

    Attributes
    ~~~~~~~~~~
        name (string):
            Name of the state
    """
    name = ""
