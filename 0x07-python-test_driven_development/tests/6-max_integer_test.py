#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_max_at_end(self):
        """tests if max value is at the end"""
        llist = [1, 2, 3, 4]
        self.assertEqual(max_integer(llist), 4)

    def test_max_at_beginning(self):
        """tests if max value is at the beginning"""
        llist = [4, 3, 2, 1]
        self.assertEqual(max_integer(llist), 4)

    def test_max_in_middle(self):
        """tests if max value is in the middle"""
        llist = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(llist), 5)

    def test_one_negative_number(self):
        """tests if it finds max even if one negative number exists"""
        llist = [1, -2, 3, 4, -5]
        self.assertEqual(max_integer(llist), 4)

    def test_negative_numbers(self):
        """
        tests if it finds max even if the list is only negative numbers
        """
        llist = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(llist), -1)

    def test_one_element(self):
        """tests if list has only one element"""
        llist = [2]
        self.assertEqual(max_integer(llist), 2)

    def test_empty_list(self):
        """tests if the list is empty"""
        llist = []
        self.assertEqual(max_integer(llist), None)


if __name__ == '__main__':
    unittest.main()
