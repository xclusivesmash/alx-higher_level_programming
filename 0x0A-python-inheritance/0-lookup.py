#!/usr/bin/python3
"""
Module 0-lookup
Implements the __dict__ method
"""


def lookup(obj):
    """Looks up attributes and methods of obj

    Args:
        obj (class): object instance.

    Returns:
        list of attributes and methods of obj.
    """
    return list(obj.__dict__)
