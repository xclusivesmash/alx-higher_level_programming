#!/usr/bin/python3
"""
Module: 4-from_json_string
Description: loads a json object.
"""
import json


def from_json_string(my_str):
    """Loads a json object: my_str."""
    return json.loads(my_str)
