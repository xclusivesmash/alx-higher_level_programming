#!/usr/bin/python3
"""Define Class Square"""


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
            size (int): public attribute (size of a square)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size is a setter function

        Args:
            value (int): size to assign to size attribute
        """
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """Prints the area of a square

        Returns:
            calculated area (int): area of a square.
        """
        return self.__size ** 2

    def __eq__(self, __value: object) -> bool:
        """checks for == between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size == __value.size

    def __ne__(self, __value: object) -> bool:
        """checks for != between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size != __value.size

    def __gt__(self, __value: object) -> bool:
        """checks for > between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size > __value.size

    def __ge__(self, __value: object) -> bool:
        """checks for >= between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size >= __value.size

    def __lt__(self, __value: object) -> bool:
        """checks for < between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size < __value.size

    def __le__(self, __value: object) -> bool:
        """checks for <= between 2 objects

        Args:
            __value (object): instance of an object.

        Returns:
            bool: true if condition met, otherwise false
        """
        if not isinstance(__value, Square):
            return NotImplemented
        return self.size <= __value.size
