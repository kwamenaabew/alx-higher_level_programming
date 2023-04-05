#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

class that defines a rectangle figure

"""


class Rectangle:
    """class Rectangle that defines a rectangle

    Attributes: none
    """

    def __init__(self, width=0, height=0):
        """
        Init method

        Attributes:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        self.width = width
        self.height = height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Property height to get height

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectange

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to get it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): The width of the rectangle

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
