#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    start = 0
    while start < x:
        try:
            print(f"{my_list[start]}", end="")
        except IndexError:
            break
        start = start + 1
    print("")
    return start
