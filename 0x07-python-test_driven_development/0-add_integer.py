#!/usr/bin/python3
""" 0-add_integer Module """

def add_integer(a, b=98):
    """
    Adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        addition of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        new_a, new_b = int(a), int(b)
        return new_a + new_b

