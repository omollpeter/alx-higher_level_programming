#!/usr/bin/python3
"""
This module contains the following function:
    is_kind_of_class: Returns True if an object is an instance of a
        class (False otherwise)
"""


def is_kind_of_class(obj, a_class):
    """
    Returns whether or not obj is an instance of a_class
    """

    return isinstance(obj, a_class)
