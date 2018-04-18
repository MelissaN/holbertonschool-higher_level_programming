#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

my_list = [-91, -90]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

my_list = [1]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
