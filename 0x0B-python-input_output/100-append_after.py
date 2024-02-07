#!/usr/bin/python3
"""
This module contains the following function:
    append_after - Appends a string after a line containing a specific
                    string

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a string after a line containing a specific string
    """

    lines = ''
    with open(filename) as f:
        for line in f:
            if search_string in line:
                line += new_string
            lines += line
    with open(filename, "w") as f:
        f.write(lines)
