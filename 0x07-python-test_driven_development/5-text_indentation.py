#!/usr/bin/python3
"""
This module contains a function that splits a text into sentences
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == "\n":
            print("\n")
            if text[i + 1] == " ":
                i += 1
        i += 1
