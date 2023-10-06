#!/usr/bin/python3
""" module containing class FileStorage that serializes and deserializes
    objects to and from Python and JSON """
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
        """ """
        return self.__objects
    
    def new(self, obj):
        """ """
        self.__objects.update([(f"1. {obj.get('__class__')}.{obj.get('id')}", obj)])
        print(f"1. {self.__objects}")
    
    def save(self):
        """ """
        print(f"2. {self.__objects}")
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """ """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        else:
            print("failed to load file")
