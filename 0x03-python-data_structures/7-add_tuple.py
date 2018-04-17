#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) is 0:
        return(tuple(map(sum, zip(tuple_a, (0,0)))))
    elif len(tuple_b) is 1:
        new = tuple_b + (0,)
        return(tuple(map(sum, zip(tuple_a, new))))
    else:
        return(tuple(map(sum, zip(tuple_a, tuple_b))))
