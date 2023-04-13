#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectnagle class that defines
Attributes: none
"""
    def __init__(self, height=0, width=0):
        """Init method for height and width private instant variables
Attributes:
width (int) : width of rectangle
height (int) : height of rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property width to get the width parameter
Returns: width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width of the rectangle
Attributes:
width (int): width of the rectangle
Raises:
TypeError: If the width is not an integer
ValueError: If the height is less than 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width

    @property
    def height(self):
        """Property height to get the height parameter
Returns: width of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """Setter for height of the rectangle
Attributes:
height (int): height of the rectangle
Raises:
TypeError: If the width is not an integer
ValueError: If the height is less than 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height
