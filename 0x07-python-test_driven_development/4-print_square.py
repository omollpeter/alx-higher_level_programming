#!/usr/bin/python3
"""
This module contains the following function:
    print_square - Prints a square using # character

"""


def print_square(size):
    """
    Prints a square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(size * "#" for i in range(size)))
