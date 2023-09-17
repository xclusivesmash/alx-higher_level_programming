#!/usr/bin/python3
"""
Module: 3-to_json_string.py
append to an existing file.
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object.

    Args:
        my_obj (obj): input object.

    Returns:
        J_format (json): JSON representation of obj.
    """
    J_format = json.dumps(my_obj)
    return J_format
