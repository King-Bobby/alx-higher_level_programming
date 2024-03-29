#!/usr/bin/python3
"""
Module 6-peak that contains function find_peak
"""


def find_peak(list_of_integers):
    """
    A function to find the largest number in a list of unsorted integers
    """
    low = 0
    high = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
