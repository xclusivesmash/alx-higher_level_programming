#!/usr/bin/python3
"""
Module: 0-read_file
Description: reads a .txt file and
prints it to stdout.
"""


def read_file(filename=""):
    """Reads filename and prints to stdout."""
    with open(filename, mode="r", encoding="utf-8") as fh:
        data = fh.read()
        print(data, end="")
    return None
