#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Class instance recognition
"""


def is_kind_of_class(obj, a_class):
    """Looks up attributes and methods of obj

    Args:
        obj (class): object instance.
        a_class (class): used to compare against

    Returns:
        True if obj is instance of a_class. Otherwise, False
    """
    return isinstance(obj, a_class)
