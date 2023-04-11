#!/usr/bin/python3

class SortedList(list):
    """
    A custom list class that inherits from the built-in list and adds
    a new method `print_sorted`
    to print the sorted list.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the list."""
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Print the sorted list."""
        sorted_list = sorted(self)
        print(sorted_list)
