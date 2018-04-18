#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()

# for row in matrix:
#     print(" ".join("{:d}".format(i) for i in row))
