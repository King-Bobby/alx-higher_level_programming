#!/usr/bin/python3
"""
Module 1-write_file that contains function write_file
"""


def write_file(filename="", text=""):
    """writes text in file "filename" and returns no of chars"""
    with open(filename, 'w') as f:
        return(f.write(text))
