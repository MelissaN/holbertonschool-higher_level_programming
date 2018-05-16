#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains method is_kind_of_class
returns True if object is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Return:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
