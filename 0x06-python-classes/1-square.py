#!/usr/bin/python3
"""
Module Square
Defines class Square with private attribute size
"""


class Square:
    """
    Class Square definition.

    Args:
        size : size of a side in square.
    """
    def __init__(self, size):
        """
        Attributes:
            size: size of a square
        """
        self.__size = size
