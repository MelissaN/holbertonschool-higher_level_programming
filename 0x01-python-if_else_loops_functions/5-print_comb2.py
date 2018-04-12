#!/usr/bin/python3
#f.o.r i in range(0, 100):
#    if i is not 99:
#        p.r.i.n.t("{:02}, ".format(i), end="")
#    else:
#        p.r.i.n.t("{:02}".format(i))
print(", ".join("{:02d}".format(i) for i in range(0, 100)))
