#!/usr/bin/python3
"""
Module 1-my_list that contains class MyList
"""


class MyList(list):
    """A class that inherits from list

    Methods:
        print_sorted: that prints the list but in sorted in ascending order
    """
    def print_sorted(self):
        """prints sorted list in ascending order"""
        print(sorted(self))
