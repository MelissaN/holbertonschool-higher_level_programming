#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = -3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = 0
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = 4
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = 5
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

my_list = [1, 2, 3, 4, 5]
idx = 6
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
