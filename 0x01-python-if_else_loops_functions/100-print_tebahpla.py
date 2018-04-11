#!/usr/bin/python3
i = 0
for n in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        print(chr(n), end='')
    else:
        print(chr(n - ord('a') + ord('A')), end='')
    i += 1
