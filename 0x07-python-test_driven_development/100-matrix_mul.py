#!/usr/bin/python3
"""
This module contains the function def matrix_mul(m_a, m_b)
"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(row) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")

    new_matrix = []
    n = 0
    for rowA in range(len(m_a)):
        llist = []
        for columnB in range(len(m_b[0])):
            for i in range(len(m_a[0])):
                n += m_a[rowA][i] * m_b[i][columnB]
            llist.append(n)
            n = 0
        new_matrix.append(llist)

    return new_matrix
