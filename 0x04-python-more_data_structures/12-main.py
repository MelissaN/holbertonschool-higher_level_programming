#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "ACC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "AZZ"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMXC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
