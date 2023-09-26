#!/usr/bin/python3
"""Module: base"""


class Base:
    """Base Class Definition
    Args:
        id (int): input integer.
    Methods:
        __init__(self, id=None)
    """
    # constants
    __nb_objects = 0

    # initialization
    def __init__(self, id: int = None):
        """Initialization method.
        Attributes:
            id (int): identification for each instance."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
