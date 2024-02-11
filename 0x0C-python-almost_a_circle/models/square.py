#!/usr/bin/python3
"""
This module contains definition of Square class which inherits
from Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instance attributes
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        Returns the unofficial string representation of the Square
        instance
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.__x,
            self.__y,
            self.__size
        )

    @property
    def size(self):
        """
        Returns the size value of Square instance
        """

        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the Square instance
        """

        return self.__size * self.__size
