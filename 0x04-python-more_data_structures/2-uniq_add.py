#!/usr/bin/python3

def uniq_add(my_list=[]):
    store = []
    for item in my_list:
        if item not in store:
            store.append(item)
    return sum(store)
