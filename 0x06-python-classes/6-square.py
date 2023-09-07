#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """Square class based on size of square

    Args:
        size (int): size of a square
        position (tuple): spaces used in printing a square
    """
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initialiation function

        attributes:
            size (int): size of a square
            position (tuple): spaces used in printing a square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter function

        Returns:
            position (tuple): position variable.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function

        Args:
            value (tuple): tuple with position values.
        """
        if type(value) is not tuple or len(value) != 2 \
            or type(value[0]) is not int or type(value[1]) is not int or \
                value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        return None

    def area(self):
        """Prints the area of a square

        Returns:
            calculated area (int): area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a sqaure using # symbols
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print("".join(" " * self.__position[0] + "#" * self.__size))
        return None
