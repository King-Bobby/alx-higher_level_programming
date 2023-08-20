#!/usr/bin/python3
"""
This module contains the function def matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    eror_message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(eror_message)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(eror_message)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(eror_message)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
