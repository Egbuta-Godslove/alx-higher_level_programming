#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    
    Args:
        matrix (list of lists): the matrix to be divided
        div (int or float): the divisor to divide the matrix by
        
    Returns:
        A new matrix containing the divided elements rounded to 2 decimal places.
        
    Raises:
        TypeError: if the input is not a matrix of integers or floats, or if div is not a number
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    # Check that each row of the matrix has the same length
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Divide each element of the matrix by the divisor
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return new_matrix

