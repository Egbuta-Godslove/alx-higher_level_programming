#!/usr/bin/python3
"""
ALX project on OOP
"""

class Rectangle:
   """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
	"""init method"""    
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):    
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
	"""del method"""    
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
