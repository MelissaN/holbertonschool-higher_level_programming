#!/usr/bin/python3
"""
14-main
"""
pascal_triangle = __import__('14-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print("Size -5 shouldn't print anything")
    print_triangle(pascal_triangle(-5))
    print("Size 0 shouldn't print anything")
    print_triangle(pascal_triangle(0))
    print("Size 1 should print [1]")
    print_triangle(pascal_triangle(1))
    print("Size 2 should print [1] , [1, 1]")
    print_triangle(pascal_triangle(2))
    print("Size 3 should print [1], [1, 1], [1, 2, 1]")
    print_triangle(pascal_triangle(3))
    print("Size 5 should print [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]")
    print_triangle(pascal_triangle(5))
