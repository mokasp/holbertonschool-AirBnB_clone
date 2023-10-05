#!/usr/bin/python3
""" Module containing the class BaseModel """

import datetime
import uuid


class BaseModel:
    """
    A class representing a BaseModel to create the AirB&B Console

    Attributes
    ~~~~~~~~~~
    id (str):
        Universally Unique Identifier
    created_at (datetime):
        Current date/time at which an instance was created
    updated_at (datetime):
        Current date/time at which an instance was updated)

    Methods
    ~~~~~~~
    save():
        Updates attribute "updated_at" with current date/time.
    to_dict():
        Returns - a dictionary containing the attributes of an instance
    """

    def __init__(self, id=0, created_at=0, updated_at=0):
        """
        Initializes the objects

        Parameters
        ~~~~~~~~~~
        id (hex):
            Universally Unique Identifier
        created_at (datetime):
            Current date/time at which an instance was created
        updated_at (datetime):
            Current date/time at which an instance was updated)
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns a string representation of BaseModel """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates attribute "updated_at" with current date/time """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Updates attribute "updated_at" with current date/time """
        attributes_dict = self.__dict__
        c_at = self.created_at.isoformat()
        u_at = self.updated_at.isoformat()
        attributes_dict.update(created_at=c_at, updated_at=u_at)
        attributes_dict.update([("__class__", self.__class__.__name__)])

        return attributes_dict
