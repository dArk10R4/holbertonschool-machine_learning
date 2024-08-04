#!/usr/bin/env python3
"""
Write a function def add_arrays(arr1, arr2): that adds two arrays element-wise:

You can assume that arr1 and arr2 are lists of ints/floats
You must return a new list
If arr1 and arr2 are not the same shape, return None
"""


def add_arrays(arr1, arr2):
    """
    elementvise sum
    """
    if len(arr1) != len(arr2):
        return None

    return [arr1[i] + arr2[i] for i in range(len(arr1))]
