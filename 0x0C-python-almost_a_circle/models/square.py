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
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the Square instance
        """

        return self.__size * self.__size

    def update(self, *args, **kwargs):
        """
        Updates the instance attributes
        """
        if args:
            len_args = len(args)
            attribs = ("width", "x", "y")
            if len_args > 1 and len_args < 5:
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
                self.__size = args[1]
            elif len_args == 3:
                self.id = args[0]
                self.__size = args[1]
                self.__x = args[2]
            else:
                self.id = args[0]
                self.__size = args[1]
                self.__x = args[2]
                self.__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    if type(value) is not int:
                        raise TypeError("width must be an integer")
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__size = value
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
        self._Rectangle__width = self.__size
        self._Rectangle__height = self.__size
        self._Rectangle__x = self.__x
        self._Rectangle__y = self.__y

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance
        """

        return dict(
            id=self.id,
            size=self.__size,
            x=self.__x,
            y=self.__y
        )
