#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = 0
    for i in range(0, len(my_list), 1):
        number = my_list[i]
        if number > maxi:
            maxi = number
    return maxi
