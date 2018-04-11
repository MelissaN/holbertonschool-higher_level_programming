#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end='')
    return(abs(number) % 10)

#    if number < 0:
#        number = number * -1
#    print("{}".format(number % 10), end='')
#    return (number % 10)
