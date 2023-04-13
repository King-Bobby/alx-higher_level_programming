#!/usr/bin/python3
"""
Module 6-load_from_json_file
that contains function load_from_json_file
"""


import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”
    arg:
        filename - name of json file"""
    with open(filename) as f:
        return json.load(f)
