#!/usr/bin/python3
"""
Module contains class Rectangle which inherits an attribute from class Base
"""


from models.base import Base


class Rectangle(Base):
    """class Base contains
    Inherited Attibute:
        id - from class Base
    Attributes:
        width       height
        x           y
    Methods:
        __init__(self, width, height, x-0, y=0, id=None)
        width(self)     width(self, value)
        height(self)    height(self, value)
        x(self)         x(self, value)
        y(self)         y(self, value)
        area(self)      display(self)
        __str__(self)   update(self, *args, **kwargs)
        to_dictionary(self)
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle shape using (#)
        and gives upward and sideways spacing based on x and y"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """Returns output [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """if args: assigns available args to the following attributes
                    in this order id, width, height, x, y
        if no args: set attributes according to kwargs"""
        if args:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.width = value
                elif idx == 2:
                    self.height = value
                elif idx == 3:
                    self.x = value
                elif idx == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic_t = {}
        dic_t["id"] = self.id
        dic_t["width"] = self.width
        dic_t["height"] = self.height
        dic_t["x"] = self.x
        dic_t["y"] = self.y
        return dic_t
