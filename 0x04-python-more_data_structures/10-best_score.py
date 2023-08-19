#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    store = ""
    for k, v in a_dictionary.items():
        if v == max(list(a_dictionary.values())):
            store = k
            break
    return store
