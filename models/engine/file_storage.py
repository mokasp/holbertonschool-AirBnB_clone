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
        stuff = self.__objects
        self.__objects = self.save_helper(stuff)
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def save_helper(self, main_dictionary):
        """ helper function to resolve serialization issue with date/time """
        keys = main_dictionary.keys()
        for item in keys:
            main_key = item
            dictionary = main_dictionary.get(main_key)
            for key in dictionary:
                if key == 'updated_at' or key == 'created_at':
                    issue = dictionary.get(key)
                    if isinstance(issue, datetime.datetime):
                        the_key = key
                        resolve = issue.isoformat()
                        dictionary.update([(the_key, resolve)])
                        main_dictionary.update([(main_key, dictionary)])
        return main_dictionary

    def reload(self):
        """ if JSON file exists, deserializes JSON file back to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                thing = json.load(file)
                self.__objects = self.reloaded_helper(thing)
                
        else:
            pass

    def reloaded_helper(self, a_dictionary):
        keys = a_dictionary.keys()
        for item in keys:
            main_key = item
            dictionary = a_dictionary.get(main_key)
            for key in dictionary:
                if key == 'updated_at' or key == 'created_at':
                    issue = dictionary.get(key)
                    if isinstance(issue, str):
                        the_key = key
                        resolve = datetime.datetime.fromisoformat(issue)
                        dictionary.update([(the_key, resolve)])
                    a_dictionary.update([(main_key, dictionary)])
        return a_dictionary
