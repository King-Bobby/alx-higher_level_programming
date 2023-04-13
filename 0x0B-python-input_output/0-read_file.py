#!/usr/bin/python3
"""
Module 0-read_write that contains function read_file
"""


def read_file(filename=""):
    """reads a file and prints it to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
