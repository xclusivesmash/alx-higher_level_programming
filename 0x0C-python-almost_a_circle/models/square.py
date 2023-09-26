#!/usr/bin/python3
"""Module: square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class Definition.
    Args:
        size (int): size of a square.
        x (int): x positional movement.
        y (int): y positional movement.
        id (int): input integer.
    Methods:
        __init__(self, size: int, x=0, y=0, id=None)
        __str__(self)
        size(self) -> getter
        size(self, value) -> setter
        update(self, *args, **kwargs)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """String representation of the object."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.__class__.__name__, self.id, self.x, self.y,
                    self.width)

    @property
    def size(self):
        """Getter: size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter: size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        return None

    def update(self, *args, **kwargs):
        """Update object attributes."""
        if args is not None and len(args) != 0:
            # working with args
            for i, _ in enumerate(args):
                if (i + 1) == 1:
                    self.id = args[i]
                elif (i + 1) == 2:
                    self.size = args[i]
                elif (i + 1) == 3:
                    self.x = args[i]
                elif (i + 1) == 4:
                    self.y = args[i]
        else:
            # working with kwargs
            for k, v in kwargs.items():
                setattr(self, k, v)
        return None
