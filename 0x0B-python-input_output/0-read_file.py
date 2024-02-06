#!/usr/bin/python3
"""
This module contain the following function
    read_file - Reads a utf8 encoded file

"""


def read_file(filename=""):
    """
    Reads a utf8 encoded file
    """

    with open(filename, encoding="utf-8") as f:
        lines = [line.strip() for line in f]
        print('\n'.join(lines))
