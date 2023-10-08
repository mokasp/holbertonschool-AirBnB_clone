#!/usr/bin/python3
""" module containing class FileStorage that serializes and deserializes
    objects to and from Python and JSON """
# Michael edited at 11:09am 10/8/23
import models
from models.base_model import BaseModel
import datetime
import json
import os


class FileStorage():
    """
    A class that serializes instances to a JSON file and deserializes JSON
    file to instances

    Class Attributes
    ~~~~~~~~~~~~~~~~
    __objects (dictionary):
        empty on initialization, but will store all objects
    __file_path (string):
        path to a JSON file

    Instance Methods
    ~~~~~~~~~~~~~~~~
    all():
        Returns - the dictionary stored in __objects.
    new(obj):
        Arguments:
            obj (self):
                A new instance of python object.
        Creates new instance in the dictionary __objects.
    save():
        Serializes __objects to JSON file.
    reload():
        If JSON file exists, deserializes JSON file back to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary stored in __objects """
        return self.__objects

    def new(self, obj):
        """ Creates new instance in the dictionary __objects

            Parameters
            ~~~~~~~~~~
            obj (self):
                A new instance of python object.
        """
        class_dictionary = obj.to_dict()
        class_name = class_dictionary.get('__class__')
        key = f"{class_name}.{obj.id}"
        self.__objects.update([(key, obj)])

    def save(self):
        """ Serializes Python objects to JSON file """
        objects_copy = self.__objects.copy()
        new_dictionary = {}
        for key in objects_copy:
            python_obj = objects_copy.get(key)
            new_dictionary[key] = python_obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dictionary, file)

    def reload(self):
        """ If JSON file exists, deserializes JSON file back to python
            objects """
        classes = {"BaseModel": BaseModel}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                loaded = json.load(file)
                for key in loaded:
                    old_value = loaded.get(key)
                    class_name = old_value.get('__class__')
                    new_value = classes[class_name](**old_value)
                    loaded.update([(key, new_value)])
                self.__objects = loaded
        else:
            pass
