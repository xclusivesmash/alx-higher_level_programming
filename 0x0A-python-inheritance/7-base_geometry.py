#!/usr/bin/python3
"""
Class: BaseGeometry
"""


class BaseGeometry:
    """Clas definition

    methods:
        area
        integer_validator
    """
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is of type int

        Args:
            name (str): input string.
            value (int): input integer.

        Returns:
            value (int): input integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
