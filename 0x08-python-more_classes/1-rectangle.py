#!/usr//bin/python3
"""
Rectangle class that defines a rectangle
based on 0-rectangle.py
"""


class Rectangle:
    """
    Empty class that defines a rectangle
    Attribute: None
    """

    def __init__(self, width=0, height=0):
        """
        Init method for class rectangle
        Attributes:
        width: width of rectangle
        height: height of rectangle
        """
        self.__width = width
        self.__heigh = height

    @property
    def height(self):
        """
        Property to get the height
        Returns:
        height (int) : The width of the Rectangle
        """
        return self.__height

    @height.setter
    def heigh(self, value):
        """
        Setter for height of the rectangle
        Attributes:
        height: The height of the rectangle
        Raises:
        TypeError: If width is not an integer
        ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self, value):
        """
        Setter for width of the Rectangle
        Attributes:
        width (int) : the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width of the rectangle
        Atrributes:
        width: The width of the rectangle
        Raises:
        TypeError: If the width is not an integer
        ValueError: If the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value
