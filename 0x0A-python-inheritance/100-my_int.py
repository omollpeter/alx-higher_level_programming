#!/usr/bin/python3
"""
This module contains MyInt class

"""


class MyInt(int):
    """
    Defines MyInt which inherits from int class
    """

    def __eq__(self, other):
        """Returns True if one instance of MyInt is not equal
        to another instance of MyInt
        """

        return not self.real == other.real

    def __ne__(self, other):
        """Returns True if one instance of MyInt is equal
        to another instance of MyInt
        """

        return not self.real != other.real
