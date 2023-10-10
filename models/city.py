#!/usr/bin/python3
""" Module containing the class City """
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class called City with a public attributes.

    Attributes
    ~~~~~~~~~~
        state_id (string):
            ID of state
        name (string):
            Name of the city
    """
    state_id = ""
    name = ""
