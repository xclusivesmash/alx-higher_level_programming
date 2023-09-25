#!/usr/bin/python3
"""Module: rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class Definition
    Args:
        width (int): width size of rectangle.
        height (int): height size of rectangle.
        x (int): x positional movement.
        y (int): y positional movement.
        id (int): input integer.
    Methods:
        __init__(self, width: int, height: int, x=0, y=0, id=None)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
    """
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initialization method.
        Attributes:
            height (int): height of the rectangle."""
        super().__init__(id)
        self.height = height

    @property
    def height(self):
        """Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter."""
        self.__height = value
        return None

    @property
    def width(self):
        """Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter."""
        self.__width = value
        return None

    @property
    def x(self):
        """Getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter."""
        self.__x = value
        return None

    @property
    def y(self):
        """Getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter."""
        self.__y = value
        return None
