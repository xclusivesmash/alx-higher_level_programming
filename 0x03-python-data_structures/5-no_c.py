#!/usr/bin/python3

def no_c(my_string):
    return "".join(m for m in my_string if m not in "cC")
