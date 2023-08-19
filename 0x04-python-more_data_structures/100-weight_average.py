#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    summation = 0
    divisor = 0
    for tuple_ in my_list:
        summation = summation + tuple_[0] * tuple_[1]
        divisor = divisor + tuple_[1]
    return (summation / divisor)
