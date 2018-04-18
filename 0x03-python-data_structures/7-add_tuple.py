#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = len(tuple_a)
    b = len(tuple_b)

    sums = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
            (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))

    return sums

# tuple_a += (0, 0)
# tuple_b += (0, 0)
# return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
