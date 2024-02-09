#!/usr/bin/python3
"""
This module contains definition for Rectangle class that inherits
from Base class

"""


from models.base import Base


class Rectangle(Base):
    """
    Defines Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instance attributes

        Args
            width (int): Width of the Rectangle instance
            height (int): Height of the Rectangle instance
            x (int): x coordinate of the Rectangle instance
            y (int): y coordinate of the Rectangle instance
            id (int): Unique id of the Rectangle instance
        """
        super().__init__(id=id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Returns the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Returns the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def width(self, height):
        self.__height = height

    @property
    def x(self):
        """Returns the x co-ordinate of a Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Returns the y co-ordinate of a Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
