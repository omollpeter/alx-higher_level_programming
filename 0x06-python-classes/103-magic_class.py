#!/usr/bin/python3
"""Contains class definition for MagicClass"""


import math


class MagicClass:
    """Defines MagicClass"""

    def __init__(self, radius=0):
        """Initializes instance attributes"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes area"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculates the circumference"""
        return 2 * math.pi * self.__radius
