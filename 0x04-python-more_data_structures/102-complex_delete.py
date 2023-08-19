#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    stored = a_dictionary.copy()
    for key_, value_ in stored.items():
        if value_ == value:
            del a_dictionary[key_]
    return a_dictionary
