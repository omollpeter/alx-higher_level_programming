#!/usr/bin/python3
"""
This module contains the following function:
    class_to_json - Converts all instance attributes in __dict__
                    to JSON
"""


import json


def class_to_json(obj):
    """
    Converts all instance attributes in __dict__ to JSON
    """

    return json.dumps(obj.__dict__)
