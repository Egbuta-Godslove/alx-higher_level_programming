#!/usr/bin/python3

class MyList(list):
    """
    A subclass of list that represents a custom list
    """
    def __init__(self):
        """
        Initializes an instance of MyList
        """
        super().__init__()

    def print_sorted_list(self):
        """
        Prints the sorted list
        """
        sorted_list = sorted(self)
        print(sorted(self))
