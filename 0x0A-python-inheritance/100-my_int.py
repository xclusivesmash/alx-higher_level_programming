#!/usr/bin/python3
"""
Class: MyInt
"""


class MyInt(int):
    """MyInt Class Definition

    Args:
        number (int): input integer

    Methods:
        __init__(self, number)
        __eq__(self, __value)
        __ne__(self, __value)
    """
    def __init__(self, number) -> None:
        """Initialization method

        Attributes:
            number (int): input integer
        """
        self.number = number

    def __eq__(self, __value) -> bool:
        """Inverts equality"""
        return self.number != __value

    def __ne__(self, __value) -> bool:
        """Inverts __ne__ magic method"""
        return self.number == __value
