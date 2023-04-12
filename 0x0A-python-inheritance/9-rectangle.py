#!/usr/bin/python3
"""
Module 9-rectangle that contains
Class BaseGeometry and class Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry

    Methods:
    area - that raises an exception
    integer_validator - that checks if value is not of correct type
    and if it is not positive
    """
    def area(self):
        """method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=0):
        """ checks if value is of correct type or positive"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class that inherits integer_validator from BaseGeometry"""
    def __init__(self, width, height):
        """initializes the class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
