#!/usr/bin/env python3
"""
that performs matrix multiplication
"""


def dot(mat1, mat2):
    """
    dot
    """
    return sum([mat1[i] * mat2[i] for i in range(len(mat1))])


def mat_mul(mat1, mat2):
    """
    matrix multiplication
    """
    if len(mat1[0]) != len(mat2):
        return None

    return [[dot(mat1[i], [row[j] for row in mat2]) for j in
            range(len(mat2[0]))] for i in range(len(mat1))]
