#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Description: creates a json obj from file.
"""
import json


def load_from_json_file(filename):
    """Creates a json obj from filename."""
    with open(filename, mode="r", encoding="utf-8") as fh:
        data = fh.read()
    return json.loads(data)
