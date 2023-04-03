#!/usr/bin/python3

class Rectangle:
	"""A class that defines a rectangle"""

	def __init__(self, width=0, height=0):
		"""Initialize a new Rectangle instance"""
		self.width = width
		self.height = height


	@property
	def __init__(self):
		"""Getter method for width"""
		return self.__width

	@property
	def width(self, value):
		"""Setter method for width"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		elif value < 0:
			raise valueError("width must be >= 0")
		else:
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
		elif value < 0:
			raise valueError(" height must be >=0")
		else:
			self.__height = value
