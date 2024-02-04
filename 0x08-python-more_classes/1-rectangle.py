#!/usr/bin/python3

class Rectangle:
    """Canvas for Personalized Designs"""

    def __init__(self, my_width=0, my_height=0):
        self.my_height = my_height
        self.my_width = my_width

    @property
    def my_width(self):
        """Retrieve canvas width"""
        return self.__width

    @my_width.setter
    def my_width(self, value):
        """Set canvas width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")

        self.__width = value

    @property
    def my_height(self):
        """Retrieve canvas height"""
        return self.__height

    @my_height.setter
    def my_height(self, value):
        """Set canvas height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")

        self.__height = value
