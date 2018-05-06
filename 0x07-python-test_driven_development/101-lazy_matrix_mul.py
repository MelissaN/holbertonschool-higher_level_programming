#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Contains method to multiply matrix using numpy module (pip3 install numpy)
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.matmul.html
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns matrix multiplied"""
    return numpy.matmul(m_a, m_b)
