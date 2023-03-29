#!/usr/bin/python3
"""
Defines class Square with private attribute size and initializes it
"""


class Square:
    """
    Defines Class square
    """

    def __init__(self, size=0):
        """
        Initalizes Square

        Attributes:
            size(int): size of a side of a square, default value is 0
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public method area: finds the area of a square using size as its sides
        """

        Sq_area = self.__size * self.__size
        return Sq_area
