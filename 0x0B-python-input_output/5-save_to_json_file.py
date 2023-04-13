#!/usr/bin/python3
"""
Module 5-save_to_json_file
It contains function save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj - object
        filename - name of text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
