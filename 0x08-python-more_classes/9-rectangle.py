#!/usr/bin/python3
"""
This module contains a class that defines Rectangle object
"""


class Rectangle:
    """Defines a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        return '\n'.join(
            self.__width * str(self.print_symbol) for n in range(self.__height)
        )

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

    def __del__(self):
        """Deletes Rectangle instance"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle) - First Rectangle instance
            rect_2 (Rectangle) - Second Rectangle instance

        Returns:
            bigger instance based on area btw rect_1 and rect_2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance of Rectangle whose width == height

        Args:
            size (int): width/height of the Rectangle instance (default
                is 0)

        Returns:
            instance of the Rectangle
        """

        return cls(size, size)
