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
    # constants
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Initialization method

        Attributes:
            width (int): input width.
            height (int): input height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self) -> str:
        """Return string representation of object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for _ in range(self.__height):
            string = string + str(self.print_symbol) * self.__width
            if _ != (self.__height - 1):
                string = string + "\n"
        return string

    def __repr__(self) -> str:
        """Return string rep of object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """object destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return None

    def __eq__(self, __value: object) -> bool:
        """Compares objects for equality"""
        if not isinstance(__value, Rectangle):
            return NotImplemented
        return self.area() == __value.area()

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Rectangle):
            return NotImplemented
        return self.area() > __value.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two instances of Rectangle class

        Args:
            rect_1 (Rectangle): first instance of Rectangle.
            rect_2 (Rectangle): second instance of Rectangle.

        Returns:
            rect_1 (Rectangle): if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
