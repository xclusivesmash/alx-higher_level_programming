#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """Square class based on size of square

    Args:
        size (int): size of a square
    """
    def __init__(self, size=0) -> None:
        """Initialiation function

        attributes:
            size (int): size of a square
        """
        self.size = size

    @property
    def size(self):
        """This functions gets the size of square

        Returns:
            __size (int): public attribute (size of a square)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size is a setter function

        Args:
            value (int): size to assign to size attribute
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return None

    def area(self):
        """Prints the area of a square

        Returns:
            calculated area (int): area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a sqaure using # symbols

        if the size attribute is zero, nothing is printed.
        """
        if self.__size == 0:
            print()
        for _ in range(0, self.__size, 1):
            for __ in range(0, self.__size, 1):
                print("#", end="")
            print()
        return None
