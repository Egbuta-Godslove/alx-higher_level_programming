#!/usr/bin/python3
"""
Defines a class Rectangle
"""
"""ALX project on OOP"""

class Rectangle:
    """A class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing the rectangle by
        setting the objet with width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
