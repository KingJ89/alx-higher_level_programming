#!/usr/bin/python3

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
                return self.__height

            def height(self, value):
                if not isinsistance(value, int):
                    raise TypeError("height must be an integer")
                elif value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

                def area(self):
                    return self.__width == 0 or self.__height == 0:
                        return 0
                    return 2 * (self.__width + self.__height)
