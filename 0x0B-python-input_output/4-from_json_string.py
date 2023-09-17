#!/usr/bin/python3
"""
Module: 4-from_json_string.py
"""


def from_json_string(my_str):
    """Returns string representation of JSON object.

    Args:
        my_str (str): input JSON string.

    Returns:
        J_format (json): string.
    """
    import json
    J_format = json.loads(my_str)
    return J_format
