#!/usr/bin/python3
"""
N queens puzzle challenge

The following program solves the N queens problem in a NxN chessboard
It involves palcing N non-attacking queens on the chessboard

"""


import sys


def nqueens():
    """
    Solves the N-queens problem

    Returns
        list of lists containing the positions of each queen on the chessboard
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    
    if ord(N) < 52: