#!/usr/bin/python3
"""
Module 101-add_attribute
"""


def add_attribute(obj, attribute, value):
    """Adds attributes

    Args:
        obj (instance): input instance
        attribute
        value (int): input int
    """
    if ('__dict__' not in dir(obj)):
        raise TypeError("can't add new attribute")
        setattr(obj, attribute, value)
    setattr(obj, attribute, value)
