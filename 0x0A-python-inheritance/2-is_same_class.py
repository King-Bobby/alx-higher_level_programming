#!/usr/bin/python3
"""
Module 2-is_same_class that contains method is_same_class
"""


def is_same_class(obj, a_class):
    """checks if object is an instance of a_class"""
    return type(obj) == a_class
