#!/usr/bin/python3
"""
Module: 6-peak
Description: Finds a peak in a list of unsorted
             integers.
"""


def find_peak(list_of_integers):
    """Finds peak value in input list."""
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    mid_ = size
    mid = size // 2
    while True:
        mid_ = mid_ // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_ // 2 == 0:
                mid_ = 2
            mid = mid + (mid_ // 2)
        elif mid_ > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_ // 2 == 0:
                mid_ = 2
            mid = mid - (mid_ // 2)
        else:
            return list_of_integers[mid]
