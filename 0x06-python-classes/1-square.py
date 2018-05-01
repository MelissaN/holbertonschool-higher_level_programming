#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: size of a side of square
        """
        self.__size = size
