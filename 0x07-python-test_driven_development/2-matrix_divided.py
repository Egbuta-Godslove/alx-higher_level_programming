def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): Initial 2D list representing the matrix.
        div (int or float): Divisor.

    Returns:
        list: New matrix containing the divided elements, rounded to 2 decimal places.
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    prev_len = 0
    for block in matrix:
        # Check if each block in the matrix is a list
        if not isinstance(block, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for element in block:
            # Check if each element in the block is an int or a float
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(block) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(block)

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform element-wise division and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]

