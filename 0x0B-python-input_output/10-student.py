#!/usr/bin/python3
"""
Class: Student
"""


class Student:
    """Class Definition

    Args:
        first_name (str): input string.
        last_name (str): input string.
        age (int): input age.
    """
    def __init__(self, first_name, last_name, age):
        """Initialization method

        Attributes:
            first_name (str): input string.
            last_name (str): input string.
            age (int): input age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict representation of JSON object"""
        if attrs is None:
            return self.__dict__
        D = {}
        for item in attrs:
            if item in self.__dict__.keys():
                D[item] = self.__dict__[item]
        return D
