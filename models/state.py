#!/usr/bin/python3
""" Module containing the class State """
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
