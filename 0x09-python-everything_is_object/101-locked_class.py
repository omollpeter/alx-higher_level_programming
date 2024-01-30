#!/usr/bin/python3
"""
This module contains class definition for LockedClass

"""


class LockedClass:
    """
    This is a class that prevents dynamic creation of instance
    attributes using __slots__ list
    """

    __slots__ = ["first_name"]
