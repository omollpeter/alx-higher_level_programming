#!/usr/bin/python3
"""
This module contains the following function:
    * lazy_matrix_mul - Multiplies two matrices using Numpy

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy
    """

    if type(m_a) is list:
        if not len(m_a):
            raise ValueError("m_a or m_b cannot be empty")
        for item in m_a:
            if type(item) is list:
                if not len(item):
                    raise ValueError("shapes (1,0) and (2,2) not aligned:" +
                                     " 0 (dim 1) != 2 (dim 0)")
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError("invalid data type for einsum")
            else:
                raise TypeError("m_a must be a list of lists")
    else:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    sizes_ma = []
    for item in m_a:
        sizes_ma.append(len(item))

    len1 = sizes_ma[0]
    for size in sizes_ma:
        if size == len1:
            continue
        else:
            raise TypeError("setting an array element with a sequence.")

    if type(m_b) is list:
        if not len(m_b):
            raise ValueError("m_a or m_b cannot be empty")
        for item in m_b:
            if type(item) is list:
                if not len(item):
                    raise ValueError("shapes (1,0) and (2,2) not aligned:" +
                                     " 0 (dim 1) != 2 (dim 0)")
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError("invalid data type for einsum")
            else:
                raise TypeError("m_b must be a list of lists")
    else:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    sizes_mb = []
    for item in m_b:
        sizes_mb.append(len(item))

    len2 = sizes_mb[0]
    for size in sizes_mb:
        if size == len2:
            continue
        else:
            raise TypeError("setting an array element with a sequence.")

    len_mb = len(m_b)
    if len1 != len_mb:
        raise ValueError("m_a and m_b don't meet criteria for multiplication")

    return np.array(m_a).dot(np.array(m_b))
