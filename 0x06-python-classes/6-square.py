#!/usr/bin/python3
"""
Defines class Square with private attribute size, position and
public attribute area and initializes them
Can also print area to stdout using "#"
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
        position(self)
        position(self, value)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initalizes Square

        Attributes:
            size(int): size of a side of a square, default value is 0
            position(int) = tuple of two positive integers
        """

        self.__size = size
        self.__position = position

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
                for n in range(self.__position[0]):
                    print(" ", end="")
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

    @property
    def position(self):
        """Getter function: to return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function: to set value of position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
