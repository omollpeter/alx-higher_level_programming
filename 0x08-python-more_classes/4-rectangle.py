#!/usr/bin/python3
"""
This module contains a class that defines Rectangle object
"""


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes instance attributes

        Args
            width (int): width of the Rectangle (default is 0)
            height (int): Height of the Rectangle (default is 0)
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def __repr__(self):
        """Returns the official string representation of Rectangle
        instance
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """Returns the unofficial string representation of Rectangle
        instance
        """

        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(self.__width * "#" for n in range(self.__height))

    @property
    def width(self):
        """Returns the width of the Rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Computes and returns the area of Rectangle instance"""

        return self.__width * self.__height

    def perimeter(self):
        """Computes and returns the perimeter of Rectangle instance"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
