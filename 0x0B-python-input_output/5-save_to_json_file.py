#!/usr/bin/python3
"""
This module contains the following function:
    save_to_json_file - Writes JSON to a file

"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes JSON to a file
    """

    if len(filename) == 0 and not isinstance(filename, str):
        return
    json_data = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_data)
