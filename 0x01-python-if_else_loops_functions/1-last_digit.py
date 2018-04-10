#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    pos = number * (-1)
else:
    pos = number

remainder = pos % 10
if remainder > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, remainder))
elif remainder is 0:
    print("Last digit of {} is {} and is 0".format(number, remainder))
else:
    print("Last digit of {} is {} and is less than 6 and is not 0".format(number, remainder))
