#!/usr/bin/python3
"""
Module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """Checks if an obj is an instance of a class
        that is inherited from a_class.

    Args:
        obj (class): object instance.
        a_class (class): used to compare against

    Returns:
        True if type(obj) is subclass of a_class. Otherwise, False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
