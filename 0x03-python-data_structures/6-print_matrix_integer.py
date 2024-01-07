#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(matrix) == 1 and len(row) == 0:
            print('')
            return
        for n in row:
            print('{:d}'.format(n), end='')
            if row.index(n) == len(row) - 1:
                print('\n', end='')
                continue
            print(" ", end='')
