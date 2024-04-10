#!/usr/bin/python3
"""
Module 0-add_integer
Description: contains one methods that returns sum of two integers
"""


def add_integer(a, b=98):
    """Computes the sum of two integers a and b.
    Args:
        a (int): first input integer
        b (int): second input integer
    Returns:
        a + b (int): sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    # cast variables to int if float
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
