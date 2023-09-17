#!/usr/bin/python3
"""
Module: 0-read_file.py
reads a file and prints it out to stdout.
"""


def read_file(filename=""):
    """reads a text file.

    Args:
        filename (textfile): input file.

    Returns:
        Nothing.
    """
    with open(filename, mode="r", encoding="utf-8") as fh:
        print(fh.read(), end="")
    return None
