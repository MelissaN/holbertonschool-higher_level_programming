#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            printed += 1
        except (TypeError, ValueError):
            continue
    print("")
    return printed
