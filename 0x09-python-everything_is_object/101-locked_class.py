#!/usr/bin/python3
"""
Defines a class LockedClass from Module 101-locked_class
"""


class LockedClass():
    """
    A class that only accepts attribute called first_name

    __slots__ is a built-in that prevents the user from dynamically creating
    new instance attributes, except the ones stated in __slots__
   """
    __slots__ = "first_name"
