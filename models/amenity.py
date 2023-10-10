#!/usr/bin/python3
""" Module containing the class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class called Amenity with a public attributes.

    Attributes
    ~~~~~~~~~~
        name (string):
            Name of the amenity.
    """
    name = ""
