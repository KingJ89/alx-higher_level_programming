#!/usr/bin/python3

"""
create class Rectangle that defines a rectangle
"""

class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self._validate_non_negative_integer("width", value)
            self.__width = value

            @property
            def height(self):
                return self.__height

            @height.setter
            def height(self, value):
                self._validate_non_negative_integer("height", value)
                self.__height = value

                def _validate_non_negative_integer(self, attibute, value):
                    if not isinstance(value, int):
                        raise TypeError(f"{attribute} must be an integer")
                    if value < 0:
                        raise ValueError(f"{attribute} must be >= 0")
                    if __name__ == "__main__":
                        rect1 = Rectangle(2, 4)
                        rect2 = Rectangle(10, 3)

                        print(rect1.__dict__)
                        print(rect2.__dict__)
