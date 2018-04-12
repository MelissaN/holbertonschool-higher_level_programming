#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} {:s}{:s}".
          format((len(sys.argv)-1),
                 "arguments" if (len(sys.argv)-1) is not 1 else "argument",
                 "." if (len(sys.argv)-1) is 0 else ":"))
    for i in range(1, len(sys.argv)):
        print ("{:d}: {:s}".format(i, sys.argv[i]))
