#!/usr/bin/env python3
"""
that concatenates two matrices along a specific axis:
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    concatenates two matrices along a specific axis
    """
    if axis == 0:
        return mat1 + mat2
    
    if len(mat1) != len(mat2):
        return None
    
    return [mat1[i] + mat2[i] for i in range(len(mat1))]