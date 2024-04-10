#!/usr/bin/python3
"""
Module: 1-rectangle
Description: Definition of rectangle as a class.
"""


class Rectangle:
    "An empty class defining a rectangle"

    def __init__(self, width=0, height=0):
        """Initialization method.
        Args:
            width (int): first arg.
            height (int): second arg.
        Returns:
            None.
        """
        self.width = width
        self.height = height
        return

    @property
    def width(self):
        """Retrives the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of rectangle
        Args:
            value (int): input value for width.
        Returns;
            Nothing.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return None

    @property
    def height(self):
        """Retrieves hight value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height
        Args:
            value (int): height value.
        Returns:
            None.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return None
