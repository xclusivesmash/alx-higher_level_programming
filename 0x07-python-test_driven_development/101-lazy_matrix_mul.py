#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns product of m_a and m_b

    Args:
        m_a (list of lists): first input matrix.
        m_b (list of lists): second input matrix.

    Returns:
        Product matrix.
    """
    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/101-lazy_matrix_mul.txt")
