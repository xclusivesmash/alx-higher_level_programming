#!/usr/bin/python3
"""
Module: 3-to_json_string
Description: json serialization.
"""
import json


def to_json_string(my_obj):
    """Serializes my_obj."""
    return json.dumps(my_obj)
