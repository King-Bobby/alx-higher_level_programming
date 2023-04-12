#!/usr/bin/python3
"""
Method 7-base_geometry that contains class BaseGeometry
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
