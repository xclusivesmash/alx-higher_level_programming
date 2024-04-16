#!/usr/bin/python3
"""
Module: 9-student
Description: defining a Student class.
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

    def to_json(self):
        """Retrieves dict repr of self."""
        return self.__dict__
