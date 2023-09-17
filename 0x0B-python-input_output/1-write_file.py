#!/usr/bin/python3
"""
Module: 1-write_file.py
write to a file.
"""


def write_file(filename="", text=""):
    """writes to a text file.

    Args:
        filename (textfile): input file.
        text (obj): input text file.

    Returns:
        count (int): bytes written to filename
    """
    count = 0
    with open(filename, mode="w", encoding="utf-8") as fh:
        count = fh.write(text)
    return count
