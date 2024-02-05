#!/usr/bin/python3
"""
This module contains class definition for:
    - BaseGeometry
    - Rectangle - Inherits from BaseGeometry

"""


class BaseGeometry:
    """
    Defines BaseGeometry
    """

    def area(self):
        """
        Raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Defines Rectangle
    """

    def __init__(self, width, height):
        """Initializes instance attributes"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns unofficial string representaion of Rectangle inst."""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Returns the official string representation"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the Rectangle instance"""

        return self.__width * self.__height
