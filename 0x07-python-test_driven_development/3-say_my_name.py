#!/usr/bin/python3
"""
Module 3-say_my_name
Contains method that prints out "My name is [full name]"
Takes in two strings: first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is [full name]"
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                               else "last_name"))
