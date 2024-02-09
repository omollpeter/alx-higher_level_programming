#!/usr/bin/python3
"""
This module contains definition for Base class

"""


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
