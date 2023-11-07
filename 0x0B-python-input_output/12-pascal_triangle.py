#!/usr/bin/python3
"""
Module: 12-pascal_triangle
Description: computes terms of Pascal tringle.
"""


def pascal_triangle(n):
    """returns a list of ints representing Pascal's triangle"""
    store = [[1], [1, 1]]
    if n <= 0:
        return []
    if n == 1:
        return store[0]
    elif n == 2:
        return store
    # count >= 3
    count = 3
    while count <= n:
        temp = [1]
        for index in range(0, len(store[count - 2]) - 1, 1):
            temp.append(store[count - 2][index] + store[count - 2][index + 1])
        temp.append(1)
        store.append(temp)
        count = count + 1
    return store
