#!/usr/bin/python3
"""
Module: 10-student
Description: Extension of module 9-student.
"""


class Student:
    """Class definition.
    Attributes:
        first_name (str): name.
        last_name (str): last name.
        age (int): age.
    Methods:
        __init__(self, first_name, last_name, age)
        to_json(self):
    """
    def __init__(self, first_name, last_name, age):
        """Initialization method.

        Args:
            first_name (str): name.
            last_name (str): last name.
            age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict repr of self."""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for item in attrs:
            if item in list(self.__dict__.keys()):
                my_dict[item] = self.__dict__[item]
        return my_dict
