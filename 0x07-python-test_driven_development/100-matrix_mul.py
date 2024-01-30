#!/usr/bin/python3
"""
This module contains the following function:
    * matrix_mul - Multiplies two matrices

"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    """

    if type(m_a) is list:
        if not len(m_a):
            raise ValueError("m_a can't be empty")
        for item in m_a:
            if type(item) is list:
                if not len(item):
                    raise ValueError("m_a can't be empty")
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError(
                            "m_a should contain only integers or floats")
            else:
                raise TypeError("m_a must be a list of lists")
    else:
        raise TypeError("m_a must be a list")

    sizes_ma = []
    for item in m_a:
        sizes_ma.append(len(item))

    len1 = sizes_ma[0]
    for size in sizes_ma:
        if size == len1:
            continue
        else:
            raise TypeError("each row of m_a must be of the same size")

    if type(m_b) is list:
        if not len(m_b):
            raise ValueError("m_b can't be empty")
        for item in m_b:
            if type(item) is list:
                if not len(item):
                    raise ValueError("m_b can't be empty")
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError(
                            "m_b should contain only integers or floats")
            else:
                raise TypeError("m_b must be a list of lists")
    else:
        raise TypeError("m_b must be a list")

    sizes_mb = []
    for item in m_b:
        sizes_mb.append(len(item))

    len2 = sizes_mb[0]
    for size in sizes_mb:
        if size == len2:
            continue
        else:
            raise TypeError("each row of m_b must be of the same size")

    len_mb = len(m_b)
    if len1 != len_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    n_mat = []
    for row in m_a:
        r_to_add = []
        for k in range(len2):
            j = k
            i = 0
            sum_rc = 0
            for col in row:
                sum_rc += col * m_b[i][j]
                i += 1
            r_to_add.append(sum_rc)
        n_mat.append(r_to_add)
    return n_mat
