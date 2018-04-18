#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 0
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = -3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 4
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 5
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1]
idx = 0
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

my_list = [1]
idx = 1
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
