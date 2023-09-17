#!/usr/bin/python3
"""
Module: 2-append_write.py
append to an existing file.
"""


def append_write(filename="", text=""):
    """appends text to a text file.

    Args:
        filename (textfile): input file.
        text (obj): input text file.

    Returns:
        count (int): bytes added to filename
    """
    count = 0
    with open(filename, mode="a", encoding="utf-8") as fh:
        count = fh.write(text)
    return count
