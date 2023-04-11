#!/usr/bin/python3
"""
Rectangle class that defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle
Attributes: none
"""
    def __init__(self, height=0, width=0):
        """
Init method for rectangle
Attributes:
width: width of the rectangle
height: height of the rectangle
"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property to retrieve the value of width
Attributes:
width: width of the rectangle
"""
        return self.__width

    @width.setter
    def width(self, value):
        """width value setter
Attributes:
width (int): width of rectangle
Raises:
TypeError: If width is not an integer
ValueError: If width is less than 0
"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property to retrieve the value of height
Attributes:
height (int): height of the rectangle
"""
        return self.__height

    @height.setter
    def height(self, value):
        """height value setter
Attributes:
height (int): height of rectangle
Raises:
TypeError: If value is not an integer
ValueError: If value is less than 0
"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
