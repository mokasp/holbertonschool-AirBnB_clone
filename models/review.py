#!/usr/bin/python3
""" Module containing the class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class called Review with a public attributes.

    Attributes
    ~~~~~~~~~~
        place_id (string):
            ID of place
        user_id (string):
            ID of user
        text (string):
            The review itself
    """
    place_id = ""
    user_id = ""
    text = ""
