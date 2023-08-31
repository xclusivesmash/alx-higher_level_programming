#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # store divisions
    index = 0
    while index < list_length:
        try:
            a = my_list_1[index]
            b = my_list_2[index]
            division = a / b
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
        index = index + 1
    return new_list
