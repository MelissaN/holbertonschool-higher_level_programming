#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    l = list_of_integers
    beg = 0
    end = len(l)-1

    if l[beg] > l[beg+1]:
        return l[beg]
    if l[end] > l[end-1]:
        return l[end]

    mid = (beg+end)//2
    if l[mid-1] < l[mid] and l[mid+1] < l[mid]:
        return l[mid]
    if l[mid] < l[mid-1]:
        return find_peak(l[beg:mid+1])
    elif l[mid] < l[mid+1]:
        return find_peak(l[mid:end+1])
    else:
        return l[beg]
