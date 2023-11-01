#!/usr/bin/python3
"""
Module 4-print_square
Prints a square using the `#` character.
"""


def print_square(size):
    """Prints a square based on size.

    Args:
        size (int): size length of a square.
    Returns:
        Nothing
    """
    # INPUT TYPE CHECK
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    # ACTUAL PRINTING STAGE
    if size == 0:
        print("", end="")
    for _ in range(0, size, 1):
        print("".join("#" * size))
    return None


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
