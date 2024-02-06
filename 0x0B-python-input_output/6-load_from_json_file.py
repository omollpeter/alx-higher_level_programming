#!/usr/bin/python3
"""
This module contains the following function:
    load_from_json_file - Creates object from json file
"""


import json


def load_from_json_file(filename):
    """
    Creates object from json file
    """

    with open(filename, encoding="utf-8") as f:
        data = json.loads(f.read())

    return data
