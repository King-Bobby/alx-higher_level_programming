#!/usr/bin/python3
"""
Module 2-append_write that contains function append_write
"""


def append_write(filename="", text=""):
    """appends text to file in filename"""
    with open(filename, 'a') as f:
        return(f.write(text))
