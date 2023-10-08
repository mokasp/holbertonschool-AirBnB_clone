#!/usr/bin/python3
""" Module containing the class BaseModel """
# kasper edited at 9:54 am 10-8-23
import models
import datetime
import uuid


class BaseModel():
    """
    A class representing a BaseModel to create the AirB&B Console

    Attributes
    ~~~~~~~~~~
    id (string):
        Universally Unique Identifier
    created_at (datetime):
        Current date/time at which an instance was created
    updated_at (datetime):
        Current date/time at which an instance was updated)

    Methods
    ~~~~~~~
    save():
        Updates attribute "updated_at" with current date/time.
        Returns - None
    to_dict():
        Returns - a dictionary containing the attributes of an instance
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the objects

        Parameters
        ~~~~~~~~~~
        id (hexadecimal):
            Universally Unique Identifier
        created_at (datetime):
            Current date/time at which an instance was created
        updated_at (datetime):
            Current date/time at which an instance was updated)
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    value = kwargs.get(key)
                    new_value = datetime.datetime.strptime(value, date_format)
                    setattr(self, key, new_value)
                elif key != '__class__':
                    setattr(self, key, kwargs.get(key))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation of BaseModel """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates attribute "updated_at" with current date/time """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Updates attribute "updated_at" with current date/time """
        attributes_dict = self.__dict__.copy()
        c_at = self.created_at
        u_at = self.updated_at
        c_at = c_at.isoformat()
        u_at = u_at.isoformat()
        attributes_dict.update(created_at=c_at, updated_at=u_at)
        attributes_dict.update([("__class__", self.__class__.__name__)])

        return attributes_dict
