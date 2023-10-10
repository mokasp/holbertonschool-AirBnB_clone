#!/usr/bin/python3
""" Module containing the class User """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class to represent a User

    Attributes
    ~~~~~~~~~~
        email (string):
            email of the User
        password (string):
            password of user
        first_name (string):
            first name of the User
        last_name (string):
            last name of the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
