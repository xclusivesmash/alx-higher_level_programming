#!/usr/bin/python3
"""
Class: Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry

    Args:
        width (int): width of rectangle.
        height (int): height of rectangle.

    Methods:
        __init__
        area
        __str__
    """
    def __init__(self, width, height):
        """Initialization method

        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area of rectangle"""
        return self.__height * self.__width

    def __str__(self) -> str:
        """Returns string representation of object"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
