#!/usr/bin/python3
"""
Module 3-say_my_name
Prints a given string
"""


def say_my_name(first_name, last_name=""):
    """Prints a first_name and last_name

    Args:
        first_name (str): input first name
        last_name (str): input last name
    Returns:
        Nothing
    """
    # INPUT TYPE CHECK
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
    return None


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/3-say_my_name.txt")
