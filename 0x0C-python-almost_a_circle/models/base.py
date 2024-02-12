#!/usr/bin/python3
"""
This module contains definition for Base class

"""


import json


class Base:
    """
    Defines Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance attributes

        Args:
            id (int): Unique id of Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries
        """

        if isinstance(list_dictionaries, (list,)) or list_dictionaries is None:
            if type(list_dictionaries) is list:
                for _ in list_dictionaries:
                    if not isinstance(_, dict):
                        raise TypeError(
                            "list_dictionaries must be a list of dictionaries"
                        )
        else:
            raise TypeError(
                "list_dictionaries must be a list of dictionaries"
            )
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        return json.dumps(list_dictionaries)
