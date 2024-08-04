#!/usr/bin/env python3
"""
calculate shape of the matrix
"""

def matrix_shape(matrix):
    """
    calculates the shape of a matrix
    """
    if type(matrix) is not list:
        return []
    return [len(matrix)] + matrix_shape(matrix[0])