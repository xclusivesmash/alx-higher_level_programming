#!/usr/bin/python3

def roman_to_int(roman_string):
    storage = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) != str or roman_string is None:
        return 0
    if roman_string == "":
        return 0
    number = 0
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in storage.keys():
            return 0
        elif storage[i] >= storage[j]:
            number = number + storage[i]
        else:
            number = number - storage[i]
    number = number + storage[roman_string[-1]]
    return number
