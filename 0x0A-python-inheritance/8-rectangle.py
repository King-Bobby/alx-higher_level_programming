#!/usr/bin/python3
"""
Module 8-rectangle that contains class Rectangle that inherits
from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits integer_validator from BaseGeometry"""
    def __init__(self, width, height):
        """initializes the class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
