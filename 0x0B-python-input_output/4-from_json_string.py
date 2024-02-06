#!/usr/bin/python3
"""
This module contains the following function:
    from_json_string - Returns an object represented by JSON string

"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by JSON string
    """

    return json.loads(my_str)
