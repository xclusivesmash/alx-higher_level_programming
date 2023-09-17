#!/usr/bin/python3
"""
Module: 5-save_to_json_file.py
"""


def save_to_json_file(my_obj, filename):
    """Writes a json string to filename.
    Args:
        my_obj (JSON): input JSON object.
        filename (obj): input filename.
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as fh:
        json.dump(my_obj, fh)
    return None
