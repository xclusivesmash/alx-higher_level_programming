#!/usr/bin/python3
"""
Class: Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class

    Args:
        size (int): input integer.

    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """Initialization method

        Attributes:
            size (int): input integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
