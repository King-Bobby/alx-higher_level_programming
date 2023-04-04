#!/usr/bin/python3
"""
Defines a class Rectangle from module 7-rectangle
"""


class Rectangle:
    """
    Defines class Rectangle

    Attributes:
        number_of_instances(int): shows how many times the class is used
        print_symbol(): symbol used to print perimeter of the rectangle
        width(int): width of the rectangle, default value is 0
        height(int): height of the rectangle, default value is 0
        value(int): value to be assigned to either width or height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initalizes class Rectangle

        Attributes:
            width(int): width of the rectangle, default value is 0
            height(int): height of the rectangle, default value is 0
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """ Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        p = self.__width + self.__height
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * p)

    def __str__(self):
        """prints the rectangle using print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            x = self.__height
            y = self.__width
            hsh = "\n".join([str(self.print_symbol) * y for n in range(x)])
            return hsh

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """deletes an instance of Rectangle()"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
