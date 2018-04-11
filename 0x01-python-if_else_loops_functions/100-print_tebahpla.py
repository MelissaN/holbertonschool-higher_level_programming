#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(i) if i % 2 == 0 else chr(i-32), end='')

# alternative method:
# for i in range(0, 26):
#    c = ord('z') - i
#    if i % 2 == 1:
#        c = (chr(c - ord('a') + ord('A')))
#    else:
#        c = chr(c)
#    print("{}".format(c), end='')
