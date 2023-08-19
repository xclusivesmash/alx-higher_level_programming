#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    stored = a_dictionary.copy()
    return {"{}".format(x): stored[x] * 2 for x in list(stored.keys())}
