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
