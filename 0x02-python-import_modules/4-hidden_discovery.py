#!/usr/bin/python3
import hidden_4
for i in (dir(hidden_4)):
    if i[0] is not "_":
        print("{:s}".format(i))
    else:
        pass
