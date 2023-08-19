#!/usr/bin/python3
"""
Module 3-say_my_name
contains one method that return first name and last name
"""


def say_my_name(first_name, last_name=""):
    """prints a string showing the first name and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
