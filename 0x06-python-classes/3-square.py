#!/usr/bin/python3
"""This module contain a single class thtt defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes instance attributes for instances of Square

        Args:
            size: Length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes area of Square instance

        Returns:
            The computed area
        """
        return self.__size * self.__size
