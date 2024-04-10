#!/usr/bin/python3
"""
Module 2-matrix_divided
Description: contains one methods that returns a new matrix in
which all elements are divided by a certaain number given by div.
"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix with div.

    Args:
        matrix (list): list of list of int or floats
        div (int or float): divisor
    Returns:
        new matrix with quotients
    """
    # ERROR MESSAGES FOR MATRIX INPUT
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(type_msg)

    # ERROR MESSAGES FOR DIV INPUT
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # CREATE AN EMPTY LIST
    store = []
    # CREATE LEN TO CHECK AGAINST FOR SIZE ERROR
    sample_len = len(matrix[0])
    size_msg = "Each row of the matrix must have the same size"
    for list_ in matrix:
        if len(list_) != sample_len:
            raise TypeError(size_msg)
        if not isinstance(list_, list):
            raise TypeError(type_msg)
        temp = []
        for num in list_:
            if not isinstance(num, (int, float)):
                raise TypeError(type_msg)
            quotient = round(num / div, 2)
            temp.append(quotient)
        store.append(temp)
        pass
    return store


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
