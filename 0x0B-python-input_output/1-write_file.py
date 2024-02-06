#!/usr/bin/python3
"""
This module contains the following function
    write_file - Writes a string to a text file

"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
