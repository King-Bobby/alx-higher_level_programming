#!/usr/bin/python3
"""
Module 3-to_json_string that contains functions to_json_string
"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (my_obj)"""
    return json.dumps(my_obj)
