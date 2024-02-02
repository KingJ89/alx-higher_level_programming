#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return self.__width

    def width(self, value):

    self._validate_non_negative_integer("width", value)
    self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        self._validate_non_negative_integer("height", value)
        self.__height = value

    def _validate_non_negative_integer(self, attribute, value):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def area(self):
        return self.heght * self.width

    def perimeter(self):
        return 2 * (self.height + self.width) if self.height != 0 and self.width != 0 else 0

    if __name__ == "__main__":
        my_rectangle = Rectangle(2, 4)
        print("Area: {} - perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

        print("--")

        my_rectangle.width = 10
        my_rectangle.height = 3
        print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

