#!/usr/bin/python3
"""
Module 9-student thtat contains class Student
"""


class Student:
    """ clas that contains a function to_json"""
    def __init__(self, first_name, last_name, age):
        """ initalizes the class Student
        Public attributes:
            first_name
            last_name
            age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
