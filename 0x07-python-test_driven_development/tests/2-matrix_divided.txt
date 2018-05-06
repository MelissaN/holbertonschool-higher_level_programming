# run test with python3 -m doctest -v ./tests/2-matrix_divided.txt

First import method to test
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

SUCCESS CASES:

Test signed and unsigned ints and floats in same size lists in list matrix:
     >>> matrix = [[1, 2, 3], [4, 5, 6.7]]
     >>> print(matrix_divided(matrix, 2))
     [[0.5, 1.0, 1.5], [2.0, 2.5, 3.35]]

     >>> matrix = [[1, 2, 3], [4, 5, 6.7]]
     >>> print(matrix_divided(matrix, float("inf")))
     [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

     >>> matrix = [[-1.5], [-2.5]]
     >>> print(matrix_divided(matrix, 2.5))
     [[-0.6], [-1.0]]

     >>> matrix = [[True], [False]]
     >>> print(matrix_divided(matrix, True))
     [[1.0], [0.0]]

FAIL CASES:

Test empty matrix:
     >>> print(matrix_divided(None, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = []
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = [[], [], []]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

Test different sized lists in matrix:
     >>> matrix = [[1, 2, 3], [4]]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: Each row of the matrix must have the same size

     >>> matrix = [[1, 2, 3], [4, 5, 6], [7]]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: Each row of the matrix must have the same size

Test matrix with other data types:
     >>> matrix = [["hey"], ["you"]]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = [[1, 2, 3], {"key" : 4}]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = [[1, 2], 3, {4, 5}]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = {1, 2, 3, 4}
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = ([1, 2], [3, 4])
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

     >>> matrix = [[1, 2], [3, (4, 5)]]
     >>> print(matrix_divided(matrix, 2))
     Traceback (most recent call last):
     ...
     TypeError: matrix must be a matrix (list of lists) of integers/floats

Test extra args:
     >>> matrix = [[1, 2, 3], [4, 5, 6.7]]
     >>> print(matrix_divided(matrix, 2, 100))
     Traceback (most recent call last):
     ...
     TypeError: matrix_divided() takes 2 positional arguments but 3 were given

Test too few args
     >>> matrix = [[1, 2], [3, 4]]
     >>> print(matrix_divided(matrix))
     Traceback (most recent call last):
     ...
     TypeError: matrix_divided() missing 1 required positional argument: 'div'

Test div as 0 or non-int or non-float:
     >>> matrix = [[1, 2], [3, 4]]
     >>> print(matrix_divided(matrix, 0))
     Traceback (most recent call last):
     ...
     ZeroDivisionError: division by zero

     >>> matrix = [[1, 2], [3, 4]]
     >>> print(matrix_divided(matrix, "2"))
     Traceback (most recent call last):
     ...
     TypeError: div must be a number
