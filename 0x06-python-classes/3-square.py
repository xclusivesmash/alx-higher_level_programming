#!/usr/bin/python3
"""
Description: Module Square
"""


class Square:
    """
    Class Square Definition.

    Args:
        size (int): size of a side in square.

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes class Square

        Attributes:
            size (int): size of a side of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes area of square

        Returns:
            area calculated from size.
        """
        return (self.__size) ** 2
