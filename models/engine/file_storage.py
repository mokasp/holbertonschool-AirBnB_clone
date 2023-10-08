#!/usr/bin/python3
""" module containing class FileStorage that serializes and deserializes
    objects to and from Python and JSON """
# kasper edited at 10:04am 10/8/23
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
    ~~~~~~~~~~
    __objects (dictionary):
        empty on initialization, but will store all objects
    __file_path (string):
        path to a JSON file

    Instance Methods
    ~~~~~~~
    all():
        Returns - the dictionary stored in __objects
    new(obj):
        creates new instance in the dictionary __objects
    save():
        serializes __objects to JSON file
    reload():
        if JSON file exists, deserializes JSON file back to __objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary stored in __objects """
        return self.__objects

    def new(self, obj):
        """ creates new instance in the dictionary __objects

            parameters
            ~~~~~~~~~~
            obj:
                object to insert into dictionary
        """
        temp_dict = obj.to_dict()
        class_name = temp_dict.get('__class__')
        key = f"{class_name}.{obj.id}"
        self.__objects.update([(key, obj)])

    def save(self):
        """ serializes Python objects to JSON file """
        temp_object = self.__objects.copy()
        new_dict = {}
        for key in temp_object:
            py_obj = temp_object.get(key)
            new_dict[key] = py_obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """ if JSON file exists, deserializes JSON file back to python
            Objects """
        temp_dict = {"BaseModel": BaseModel}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                loaded = json.load(file)
                for key in loaded:
                    thing = loaded.get(key)
                    value = temp_dict[thing.get('__class__')](**thing)
                    loaded.update([(key, value)])
                self.__objects = loaded
        else:
            pass
