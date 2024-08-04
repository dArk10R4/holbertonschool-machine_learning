#!/usr/bin/env python3
"""
Matrix transpose
"""


def matrix_transpose(matrix):
    """
    Transpose a matrix
    """

    return [ [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))