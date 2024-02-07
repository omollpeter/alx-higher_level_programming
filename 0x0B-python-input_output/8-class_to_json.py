#!/usr/bin/python3
"""
This module contains the following function:
    class_to_json - Converts all instance attributes in __dict__
                    to JSON
"""


def class_to_json(obj):
    """
    Converts all instance attributes in __dict__ to JSON
    """

    return obj.__dict__
