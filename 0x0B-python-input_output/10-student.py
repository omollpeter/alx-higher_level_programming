#!/usr/bin/python3
"""
This module contains class definition for Student

"""


class Student:
    """
    Defines Student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation of Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dictionary[key] = value
            return dictionary
