#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            result += (int(sys.argv[i]))
    print("{:d}".format(result))

# import sys
# print("{:d}".format(sum(int(n) for n in sys.argv[1:])))
