#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix), 1):
        for j in range(0, len(matrix[i]), 1):
            if j != (len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print()
    return None
