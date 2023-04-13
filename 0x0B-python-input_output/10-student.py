#!/usr/bin/python3
"""
Module 10-student that contains class Student
"""


class Student:
    """Class Student that contains function to_json"""
    def __init__(self, first_name, last_name, age):
        """Initializes class Student
        Public attributes:
            first_name
            last_name
            age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance or
        only attribute names contained in the list attrs
        Arg:
            attrs - is a list of strings"""
        _dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__.keys():
                    _dict[i] = self.__dict__[i]
            return _dict
