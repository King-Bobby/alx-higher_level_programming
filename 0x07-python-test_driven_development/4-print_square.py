#!/usr/bin/python3
"""
Moduule contains a function def print_square(size):
"""


def print_square(size):
    """a function that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise ValueError("size must be an integer")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print("\n", end="")
        i += 1
