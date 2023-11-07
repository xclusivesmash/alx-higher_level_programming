#!/usr/bin/python3
"""
Module: 2-append_write
Description: append text to a file.
"""


def append_write(filename="", text=""):
    """Append text to filename."""
    with open(filename, mode="a", encoding="utf-8") as fh:
        fh.write(text)
    return len(text)
