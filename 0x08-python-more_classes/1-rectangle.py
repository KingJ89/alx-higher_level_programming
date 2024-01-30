#!/usr/bin/python3
from main import Rectangle
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        def width(self):
            return self.__width

        def width(self, value):
            if not isinsistance(value, int):
                raise TypeError("width must be integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
                self.__width = value

                def height(self):
                    return self.height

                def height(self, value):
                    if not isinsance(value, int):
                        raise TypeError("height must be an integer")
                    elif Value < 0:
                        else:
                            self.__height = value
