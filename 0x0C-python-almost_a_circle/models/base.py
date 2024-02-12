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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"

        if isinstance(list_objs, (list,)) or list_objs is None:
            if type(list_objs) is list:
                for _ in list_objs:
                    if not isinstance(_, Base):
                        raise TypeError(
                            "list_objs must be a list of instances that" +
                            " inherits from Base or None"
                        )
        else:
            raise TypeError(
                "list_objs must be a list of instances that" +
                " inherits from Base or None"
            )

        with open(filename, "w", encoding="utf-8") as file:
            list_dictionaries = []
            if list_objs is None or not len(list_objs):
                file.write("[]")
            else:
                for obj in list_objs:
                    dictionary = obj.to_dictionary()
                    list_dictionaries.append(dictionary)
                data_to_save = Base.to_json_string(list_dictionaries)
                file.write(data_to_save)
