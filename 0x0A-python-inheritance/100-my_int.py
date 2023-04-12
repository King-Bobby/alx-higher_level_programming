#!/usr/bin/python3
"""
Module 100-my_int that contains clas MyInt
"""


class MyInt(int):
    """class that returns inverse of == and !=
    Note:
        __eq__returns True if two numbers are equal
        __ne__ return True if two numbers are not equal
    """
    def __init__(self, number):
        """initializes the class"""
        self.num = number

    def __ne__(self, new_num):
        """returns true if the numbers are equal"""
        return self.num == new_num

    def __eq__(self, new_num):
        """returns true if the numbers are not equal"""
        return self.num != new_num
