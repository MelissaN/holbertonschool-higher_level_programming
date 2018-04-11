#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c

# see byte code by uncommenting next two lines and running ./<filename>
# import dis
# print(dis.dis(magic_calculation))
