#!/usr/bin/python3
"""
This module contains the function is_instance_of_class.
"""


def is_instance_of_class(instance, class_type):

    """
    This function checks if the given instance is an
    instance of the specified class.

    Args:
    instance: The instance to check
    class_type: The class to check against
:wq

    Returns:
    True if the instance is an instance of the specified class,
    False otherwise.
    """
    if type(instance) is not class_type:
        return False
    else:
        return True
