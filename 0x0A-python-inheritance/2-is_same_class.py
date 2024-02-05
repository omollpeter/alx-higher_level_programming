#!/usr/bin/python3
"""
This module contains the following function:
    is_same_class: Returns True if an object is an instance of a class
        (False otherwise)
"""


def is_same_class(obj, a_class):
    """
    Returns whether or not obj is an instance of a_class
    """

    return isinstance(obj, a_class)
