#!/usr/bin/python3
"""
Module 0-lookup

Contains method lookup that returns list of object's attribute and methods
"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    return dir(obj)
