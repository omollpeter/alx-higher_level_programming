#!/usr/bin/python3
"""
This module contains the following function:
    inherits_from: Returns True if an object is a subclass of a
        class (False otherwise)
"""


def inherits_from(obj, a_class):
    """
    Returns whether or not obj is a subclass of a_class
    """

    if type(obj) is a_class:
        return False
    return issubclass(obj.__class__, a_class)
