#!/usr/bin/python3
"""
This module contains the following class:
    MyList: defines a class that inherits from list

"""


class MyList(list):
    """
    Defines a class that inherits from class list
    """

    def print_sorted(self):
        """
        prints a sorted list
        """

        print(sorted(self))
