#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in set(my_list):
        total += i
    return(total)

# return (sum(set(my_list)))
