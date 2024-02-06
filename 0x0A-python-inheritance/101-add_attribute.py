#!/usr/bin/python3
"""
This module contains the following function:
    add_attribute - Adds a new attribute to an object if possible

"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible
    """

    setattr(obj, attr, value)
