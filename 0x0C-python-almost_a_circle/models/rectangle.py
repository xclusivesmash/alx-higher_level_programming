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
        height(self) -> getter
        height(self, value) -> setter
        width(self) -> getter
        width(self, value) -> setter
        x(self) -> getter
        x(self, value) -> setter
        y(self) -> getter
        y(self, value) -> setter
        area(self)
        display(self):
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)
    """
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initialization method.
        Attributes:
            height (int): height of the rectangle."""
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def height(self):
        """Getter: height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        return None

    @property
    def width(self):
        """Getter: width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        return None

    @property
    def x(self):
        """Getter: x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter: x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        return None

    @property
    def y(self):
        """Getter: y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter: y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        return None

    def area(self):
        """Area calculation."""
        return self.__height * self.__width

    def display(self):
        """Prints to STDOUT the rectangle using #."""
        print("\n" * self.y, end="")
        string = "".join(" " * self.x + "#" * self.__width + "\n"
                         for _ in range(self.__height))
        print(string, end="")
        return None

    def __str__(self):
        """String representation."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}" \
            .format(self.__class__.__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def update(self, *args, **kwargs):
        """Update object attributes"""
        if args is not None and len(args) != 0:
            # working with args
            for i, _ in enumerate(args):
                if (i + 1) == 1:
                    self.id = args[i]
                elif (i + 1) == 2:
                    self.width = args[i]
                elif (i + 1) == 3:
                    self.height = args[i]
                elif (i + 1) == 4:
                    self.x = args[i]
                elif (i + 1) == 5:
                    self.y = args[i]
        else:
            # working with kwargs
            for k, v in kwargs.items():
                setattr(self, k, v)
        return None

    def to_dictionary(self):
        """Dictionary representation."""
        D = dict()
        D["id"] = self.id
        D["width"] = self.width
        D["height"] = self.height
        D["x"] = self.x
        D["y"] = self.y
        return D
