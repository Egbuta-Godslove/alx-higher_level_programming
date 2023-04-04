#!/usr/bin/python3
"""
The N queens puzzle is the challen noge of placing N non-attacking queens on an N×N chessboard. 
Write a program that solves the N queens problem
"""
import sys

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        return 1
    if N < 4:
        print("N must be at least 4")
        return 1
     
    def is_valid(board, row, col):
        for r in range(row):
            if board[r] == col or \
               board[r] - r == col - row or \
               board[r] + r == col + row:
                return False
        return True
    
    def solve(board, row):
        if row == N:
            print(' '.join(str(i+1) for i in board))
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row+1)
    
    board = [-1] * N
    solve(board, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(N)
