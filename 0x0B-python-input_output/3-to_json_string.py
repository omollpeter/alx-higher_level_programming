#!/usr/bin/python3
"""
This module contains the following function:
    to_json_string - Returns JSON representation of an object

"""


import json


def to_json_string(my_obj):
    """
    Returns JSON representation of an object
    """

    return json.dumps(my_obj)
