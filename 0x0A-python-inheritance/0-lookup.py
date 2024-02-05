#!/usr/bin/python3
"""
This module contains the following function:
    lookup: Lists available methods and attributes of an object

"""


def lookup(obj):
    """
    Returns the list of available methods and attributes of an object
    """

    return dir(obj)
