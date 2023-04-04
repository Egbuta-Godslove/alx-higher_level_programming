#!/usr/bin/python3

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, key, value):
        if key != 'first_name' or not hasattr(self, 'first_name'):
            raise AttributeError(f"Cannot set attribute '{key}' on LockedClass")
        super().__setattr__(key, value)
