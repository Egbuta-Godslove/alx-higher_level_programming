#!/usr/bin/python3

class LockedClass:
    __slots__ = ('__first_name')

    def __init__(self, first_name):
        self.__first_name = first_name

    @property
    def first_name(self):
        return self.__first_name
