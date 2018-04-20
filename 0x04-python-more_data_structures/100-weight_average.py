#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    frequency = 0
    for tup in my_list:
        (weight, occurence) = tup
        total += (weight * occurence)
        frequency += occurence
    return (total/frequency)
