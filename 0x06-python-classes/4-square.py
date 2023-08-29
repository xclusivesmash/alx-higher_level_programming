#!/usr/bin/python3
"""
Description: Module Class.
"""


class Square:
    """
    Class Square Definition.
    """

    def __init__(self, size=0):
        """
        Initialize class Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Sizez the siz eof square based on __size attribute.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Handles exceptions based on value.

        Args:
            value: set size to value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return:
            The current area of the square.
        """
        return (self.__size ** 2)
