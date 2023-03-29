#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, TypeError, ZeroDivisionError, ValueError) as eror:
        stderr.write("Exception: {}\n".format(eror))
        return None
