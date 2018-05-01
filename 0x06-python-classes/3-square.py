#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size and public attribute area
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            __size (int): size of a side of square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        return (self.__size)**2
