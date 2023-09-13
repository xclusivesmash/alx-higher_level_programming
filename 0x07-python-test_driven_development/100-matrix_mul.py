#!/usr/bin/python3
"""
Module 100-matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Computes matrix multiplications based on m_a and m_b

    Args:
        m_a (list of lists): first input matrix.
        m_b (list of lists): second input matrix.

    Returns:
        resultant matrix
    """
    # INPUT TYPE CHECK
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    base_len = len(m_a[0])
    for r in m_a:
        for num in r:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(r) != base_len:
            raise TypeError("each row of m_a must should be of the same size")
        if len(r) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for r in m_b:
        for num in r:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(r) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
    store = []
    summa = 0
    for x in range(0, len(m_a), 1):
        temp = []
        for xx in range(0, len(m_b[0]), 1):
            for index in range(0, len(m_a[0]), 1):
                summa = summa + m_a[x][index] * m_b[index][xx]
            temp.append(summa)
            summa = 0
        store.append(temp)
    return store


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/100-matrix_mul.txt")
