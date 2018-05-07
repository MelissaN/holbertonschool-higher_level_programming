# run test with python3 -m doctest -v ./tests/100-matrix_mul.txt

First import method to test
>>> matrix_mul = __import__('100-matrix_mul').matrix_mul

SUCCESS CASES:

Test signed and unsigned ints and floats in same size lists in list matrix:
     >>> m_a = [[1, 2], [3, 4]]
     >>> m_b = [[2, 0], [1, 2]]
     >>> print(matrix_mul(m_a, m_b))
     [[4, 4], [10, 8]]

     >>> m_a = [[-2.0, -3.0]]
     >>> m_b = [[-2.0], [-4.0]]
     >>> print(matrix_mul(m_a, m_b))
     [[16.0]]

FAIL CASES:

Test empty matrix:
     >>> m_a = []
     >>> m_b = [[2, 0], [1, 2]]
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     ValueError: m_a can't be empty

     >>> m_a = [[2, 0], [1, 2]]
     >>> m_b = []
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     ValueError: m_b can't be empty

     >>> m_a = [[2, 0], [1, 2]]
     >>> m_b = [[]]
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     ValueError: m_b can't be empty

Test different sized lists in matrix:
     >>> m_a = [[1, 2], [1, 2]]
     >>> m_b = [[1, 2], [1, 2, 3, 4]]
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     TypeError: each row of m_b must should be of the same size

     >>> m_a = [[1, 2], [1, 2, 3, 4]]
     >>> m_b = [[1, 2], [1, 2]]
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     TypeError: each row of m_a must should be of the same size

Test matrix with other data types:
     >>> m_a = [["hey"], ["you"]]
     >>> print(matrix_mul(m_a, m_a))
     Traceback (most recent call last):
     ...
     TypeError: m_a should contain only integers or floats

     >>> m_a = (1, 2)
     >>> m_b = [[1, 2], [1, 2]]
     >>> print(matrix_mul(m_a, m_b))
     Traceback (most recent call last):
     ...
     TypeError: m_a must be a list
