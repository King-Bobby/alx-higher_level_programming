#!/usr/bin/python3
"""
Module contains Class Square that inherits Class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square contains
    Attributes:
        size - one side of a square
        x, y, id
    Inherited Methods:
        Base.__init__(self, id=None)
        Rectangle.__init__(self, width, height, x-0, y=0, id=None)
        width(self)     width(self, value)
        height(self)    height(self, value)
        x(self)         x(self, value)
        y(self)         y(self, value)
        area(self)      display(self)
        __str__(self)   update(self, *args, **kwargs)
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        size(self)      size(self, value)
        __str__(self)   update(self, *args, **kwargs)
        to_dictionary(self)
        """
    def __init__(self, size, x=0, y=0, id=None):
        """Initailizes the class Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """if args: assigns available args to the following attributes
                    in this order id, size, x, y
        if no args: set attributes according to kwargs"""
        if args:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.size = value
                elif idx == 2:
                    self.x = value
                elif idx == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic_t = {}
        dic_t["id"] = self.id
        dic_t["size"] = self.size
        dic_t["x"] = self.x
        dic_t["y"] = self.y
        return dic_t
