#!/usr/bin/python3
"""
Module 0-add_integer
which contains one method that returns the sum of two numbers
"""


def add_integer(a, b=98):
    """returns the sum of a and b as int"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
