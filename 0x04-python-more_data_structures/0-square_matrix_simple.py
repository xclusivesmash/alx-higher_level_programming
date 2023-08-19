#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    store = []
    for i in range(0, len(matrix), 1):
        temp = list(map((lambda x: x ** 2), matrix[i]))
        store.append(temp)
    return store
