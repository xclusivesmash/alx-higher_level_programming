#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys_ = sorted(list(a_dictionary.keys()))
    for item in keys_:
        print("{}: {}".format(item, a_dictionary[item]))
    return None
