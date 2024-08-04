#!/usr/bin/env python3
"""
Matrix transpose
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix
    """

    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
