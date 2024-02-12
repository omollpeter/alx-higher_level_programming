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
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
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
    def width(self, wid):
        if type(wid) is not int:
            raise TypeError("width must be an integer")
        if wid <= 0:
            raise ValueError("width must be > 0")
        self.__width = wid

    @property
    def height(self):
        """Returns the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns the x co-ordinate of a Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns the y co-ordinate of a Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Computes and returns the area of the Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance, taking the
        coordinates into consideration
        """
        print("\n" * self.__y, end="")
        for n in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """
        Returns the unofficial string representation of Rectangle
        instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """
        Updates the instance attributes
        """
        if args:
            len_args = len(args)
            attribs = ("width", "height", "x", "y")
            if len_args > 1 and len_args < 6:
                for i in range(1, len_args):
                    if type(args[i]) is not int:
                        raise TypeError(f"{attribs[i - 1]} must be an integer")

                    if i <= 2:
                        if args[i] <= 0:
                            raise ValueError(f"{attribs[i - 1]} must be > 0")
                    else:
                        if args[i] < 0:
                            raise ValueError(f"{attribs[i - 1]} must be >= 0")
            elif len_args > 5:
                raise IndexError("too many arguments")

            if len_args == 1:
                self.id = args[0]
            elif len_args == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len_args == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len_args == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            return
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    if type(value) is not int:
                        raise TypeError("width must be an integer")
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                elif key == "height":
                    if type(value) is not int:
                        raise TypeError("height must be an integer")
                    if value <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = value
                elif key == "x":
                    if type(value) is not int:
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                elif key == "y":
                    if type(value) is not int:
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value
                else:
                    raise KeyError("invalid attribute")
        else:
            raise IndexError("length of args or kwargs must be > 0")

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance
        """

        return dict(
            id=self.id,
            width=self.__width,
            height=self.__height,
            x=self.__x,
            y=self.__y
        )
