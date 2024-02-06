#!/usr/bin/python3
"""
This module contains the following function
    append_write - Appends a string to the end of text file

"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
