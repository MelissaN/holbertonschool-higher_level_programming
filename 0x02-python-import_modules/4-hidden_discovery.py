#!/usr/bin/python3
import hidden_4
for i in (dir(hidden_4)):
    if not i.startswith("__"):
        print("{:s}".format(i))
