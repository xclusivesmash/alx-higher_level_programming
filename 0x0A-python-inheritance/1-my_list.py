#!/usr/bin/python3
"""
Definition of MyList
Inherits from built-in list class.
"""


class MyList(list):
    """MyList Class Definition"""
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))
