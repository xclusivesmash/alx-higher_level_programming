#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_ = ""
    maxi = 0
    for k, v in a_dictionary.items():
        if v > maxi:
            maxi = v
            store = k
    return store
