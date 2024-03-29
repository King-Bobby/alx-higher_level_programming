#!/usr/bin/python3
"""
Module 8-class_to_json that contains function class_to_json
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    Arg:
        obj - is an instance of a Class"""
    return obj.__dict__
