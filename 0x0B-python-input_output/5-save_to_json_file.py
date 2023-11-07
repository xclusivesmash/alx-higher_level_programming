#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Description: writes a json obj to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj to filename."""
    with open(filename, mode="w", encoding="utf-8") as fh:
        fh.write(json.dumps(my_obj))
    return None
