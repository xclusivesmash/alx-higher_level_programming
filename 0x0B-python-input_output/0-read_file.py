#!/usr/bin/python3
"""
Module: 0-read_file.py
reads a file and prints it out to stdout.
"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as fh:
        print(fh.read())
    return None
