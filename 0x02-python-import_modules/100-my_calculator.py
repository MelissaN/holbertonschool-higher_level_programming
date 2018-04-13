#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if (len(argv) != 4) or ((argv[1].isdigit() is False)
                            or (argv[3].isdigit() is False)):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if (argv[2] is not "+" and argv[2] is not "-" and argv[2] is not "*" and
            argv[2] is not "/"):
        print("{:s}".format(
            "Unknown operator. Available operators:+, -, * and /"))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print("{:s} {:s} {:s} = ".format(argv[1], argv[2], argv[3]), end="")
    if (argv[2] == "+"):
        print("{:d}".format(add(a, b)))
    elif (argv[2] == "-"):
        print("{:d}".format(sub(a, b)))
    elif (argv[2] == '*'):
        print("{:d}".format(mul(a, b)))
    else:
        print("{:d}".format(div(a, b)))
