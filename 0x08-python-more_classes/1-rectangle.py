#!/usr/bin/python3
"""
Class name: Rectangle
Used to create rectangles based on width and height.
"""


class Rectangle:
    """Definition of rectangle shape with operations.

    Args:
        width (int): input width.
        height (int): input height.
    """

    def __init__(self, width=0, height=0) -> None:
        """Initialization method

        Attributes:
            width (int): input width.
            height (int): input height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): input width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return None

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): input height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return None
