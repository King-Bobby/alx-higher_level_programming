#!/usr/bin/python3
"""
Module contains class Base
"""

import json

class Base:
    """class contains
    Attributes:
        __nb_objects - a private attribute
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """initalizes class Base,
        sets id or increments class attribute and sets as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs into a file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))
