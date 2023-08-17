#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    store = my_list.copy()
    if idx < 0:
        return store
    if idx >= len(my_list):
        return store
    store[idx] = element
    return store
