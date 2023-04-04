#!/usr/bin/python3

def magic_string(n):
    
    Args:
        n (int): The number of iterations.

    Returns:
        str: A string containing "BestSchool" reapeat n times for each iteration.
    
    result = " "    
    for i in range(1, n+1):
        result += "BestSchool" *i
    return result

