#!/usr/bin/env python3
"""
Matrix transpose
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix
    """

    return [matrix[j][i] for i in range(len(matrix[0])) for j in range(len(matrix))]
