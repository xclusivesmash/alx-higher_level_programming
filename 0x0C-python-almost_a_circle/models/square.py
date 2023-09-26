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
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the object."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.__class__.__name__, self.id, self.x, self.y,
                    self.width)
