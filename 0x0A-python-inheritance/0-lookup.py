#!/usr/bin/python3
"""
The lookup function container
"""


def lookup(object_to_inspect):

    """
    Args:
        object_to_inspect: object whose attributes and methods to inspect
        Returns: a list of available attributes and methods of the object
    """
    return dir(object_to_inspect)
