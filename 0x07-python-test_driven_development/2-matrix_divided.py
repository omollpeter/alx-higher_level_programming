#!/usr/bin/python3
"""
This module contains the following function:
    * matrix_divided - Divides all the elements in a matrix by
        integer or float
"""


def matrix_divided(matrix, div):
    """
    Divides the elements of a matrix by an integer or float
    """

    if type(matrix) is list:
        for item in matrix:
            if type(item) is list:
                for a in item:
                    if type(a) is not int and type(a) is not float:
                        raise TypeError(
                            "matrix must be a matrix (list of lists)" +
                            " of integers/floats"
                        )
            else:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of" +
                    " integers/floats"
                )
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of" +
            " integers/floats"
        )

    sizes = []
    for item in matrix:
        sizes.append(len(item))

    len1 = sizes[0]
    for size in sizes:
        if size == len1:
            continue
        else:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
    if isinstance(div, (int, float)):
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")

    mat = matrix.copy()
    return list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)),
            mat))
