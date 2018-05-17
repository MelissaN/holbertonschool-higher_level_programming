#!/usr/bin/python3
"""
Module 2-read_lines

Contains function that reads n lines and prints to stdout
"""


def read_lines(filename="", nb_lines=0):
    """reads n lines and prints to stdout
    Print:
        n lines: if n
        entire file: if n is less than 1 or greater than lines in file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            while nb_lines:
                print(f.readline(), end="")
                nb_lines -= 1
