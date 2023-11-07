#!/usr/bin/python3
"""
Module: 1-write_file
Description: write text to a file.
"""


def write_file(filename="", text=""):
    """Write text to a .txt file."""
    with open(filename, mode="w", encoding="utf-8") as fh:
        fh.write(text)
    return len(text)
