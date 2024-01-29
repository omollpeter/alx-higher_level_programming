#!/usr/bin/python3
"""
This module contains the following function:
    * add_integer - Returns the sum between two integers, two floats
                    or an int and a floatIt can also be imported as a module
"""


def add_integer(a, b=98):
    """
    Addition function
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
