#!/usr/bin/python3
"""
Module: 100-append_after
Description: replaces text after a string match
in a text file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after search_string in filename."""
    with open(filename, mode="r", encoding="utf-8") as fh:
        data = fh.readlines()
    with open(filename, mode="w", encoding="utf-8") as fh:
        for line in data:
            fh.write(line)
            if search_string in line:
                fh.write(new_string)
    return None
