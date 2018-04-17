#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 0
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 4
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 5
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 6
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = -3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

my_list = [1]
idx = 1
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
