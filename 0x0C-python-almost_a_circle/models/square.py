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
        __str__(self)"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.size)
