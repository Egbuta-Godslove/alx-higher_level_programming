#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. 
Write a program that solves the N queens problem.
"""

import sys

def nqueens(n):
    if not n.isnumeric():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        for r, c in enumerate(board):
            if c == col or r - c == row - col or r + c == row + col:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            print(",".join(str(c + 1) for c in board))
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    board = [-1] * n
    backtrack(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
