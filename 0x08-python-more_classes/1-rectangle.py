#!/usr/bin/python3
"""
Defines a class Rectangle from module 1-rectangle
"""


class Rectangle:
    """
    Defines class Rectangle

    Attributes:
        width(int): width of the rectangle, default value is 0
        height(int): height of the rectangle, default value is 0
        value(int): value to be assigned to either width or height
    """
    def __init__(self, width=0, height=0):
        """
        Initalizes class Rectangle
        
        Attributes:
            width(int): width of the rectangle, default value is 0
            height(int): height of the rectangle, default value is 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """It returns the value of height"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        It sets the value for width

        Attributes:
            value(int): the value to be assigned to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """It returns the value of height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        It sets the value for height
        
        Attributes:
            value(int): the value to be assigned to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
