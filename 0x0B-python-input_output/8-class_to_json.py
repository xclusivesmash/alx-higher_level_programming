#!/usr/bin/python3
"""
Module: 8-class_to_json
Description: returns dictionary representation.
"""


def class_to_json(obj):
    """Returns dict repr of obj."""
    return obj.__dict__
