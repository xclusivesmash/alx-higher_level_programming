#!/usr/bin/python3
"""
Module: 6-load_from_json_file.py
"""


def load_from_json_file(filename):
    """loads data from a json file.
    Args:
        filename (obj): input filename.

    Returns:
        JSON object.
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as fh:
        OBJECT = json.load(fh)
    return OBJECT
