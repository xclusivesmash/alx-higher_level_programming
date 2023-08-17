#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    store = []
    check = False
    for i, number in enumerate(my_list):
        store.append(number % 2 == 0)
    return store
