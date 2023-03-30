#!/usr/bin/python3
"""
Defines class Square with private attribute size and initializes it
"""


class Square:
    """
    Defines Class square

    Functions:
        __init__(self, size)
        area(self)
        size(self)
        size(self, value)
        my_print(self)
    """
    def __init__(self, size=0):
        """
        Initalizes Square

        Attributes:
            size(int): size of a side of a square, default value is 0
        """

        self.__size = size

    def area(self):
        """
        Public method area: finds the area of a square using size as its sides
        """

        Sq_area = self.__size * self.__size
        return Sq_area

    def my_print(self):
        """ Public Method: that prints in stdout
        the square with the character (#)"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """Getter function: To return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function: To set size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
