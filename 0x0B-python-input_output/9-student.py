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

    def to_json(self):
        """Returns dict representation of JSON object"""
        return Student(self.first_name, self.last_name, self.age).__dict__
