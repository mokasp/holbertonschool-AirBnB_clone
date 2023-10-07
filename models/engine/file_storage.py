#!/usr/bin/python3
""" module containing class FileStorage that serializes and deserializes
    objects to and from Python and JSON """
# kasper edited at 9:50am 10/7/23
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
    save_helper():
        helper function to resolve serialization issue with date/time
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
        key = f"{obj.get('__class__')}.{obj.get('id')}"
        self.__objects.update([(key, obj)])

    def save(self):
        """ serializes __objects to JSON file """
        self.save_helper()
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def save_helper(self):
        """ helper function to resolve serialization issue with date/time """
        keys = self.__objects.keys()
        print(f" __objects {self.__objects}")
        for item in keys:
            main_key = item
        dictionary = self.__objects.get(main_key)
        for key in dictionary:
            if key == 'updated_at':
                issue = dictionary.get(key)
        resolve = issue.isoformat()
        dictionary.update([("updated_at", resolve)])
        self.__objects.update([(main_key, dictionary)])

    def reload(self):
        """ if JSON file exists, deserializes JSON file back to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
        else:
            pass
