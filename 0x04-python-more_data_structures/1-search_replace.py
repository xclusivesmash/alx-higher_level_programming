#!/usr/bin/python3

def search_replace(my_list, search, replace):
    store = my_list.copy()
    for i in range(0, len(store), 1):
        item = store[i]
        if search == item:
            store[i] = replace
    return store
