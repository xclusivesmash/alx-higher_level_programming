#!/usr/bin/python3
"""Define Class MagicClass
"""
import math


class MagicClass:
    """Initialize and define methods area and circumference
    
    Args:
        radius (int): input radius
    """
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calcualte circumference"""
        return 2 * math.pi * self.__radius
