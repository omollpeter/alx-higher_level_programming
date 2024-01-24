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

    @property
    def size(self):
        """Returns the value of size of a Square instance"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __eq__(self, other):
        """Compares if two instances of the same class are equal

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """Compares if an instance is less than other instance of the same
        class

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if an instance is less than or equal to other instance of
        the same

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if an instance is greater than other instance of the same
        class

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if an instance is greater than or equal to other instance
        of the same

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """Compares if two instaces of the same class are not equal

        Args:
            other: Instance to compare with current instace
        Returns:
            bool: True of False
        """
        return self.area() != other.area()

    def area(self):
        """Computes area of Square instance

        Returns:
            The computed area
        """
        return self.__size * self.__size
