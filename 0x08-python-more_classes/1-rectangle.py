#!/usr/bin/python3
"""class Rectangle that defines a rectangle by
"""


class Rectangle:
    """class Rectangle defines a rectangle
    Attributes: none
    """
    def __init__(self, width=0, height=0):
        """ Rectangle __init__ method

        Args: private instance attributes:
            width: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height

    # property decorator to retrieve width
    @property
    def width(self):
        """width getter method
        """
        return self.__width

    # property decorator to set width
    @width.setter
    def width(self, value):
        """width setter method
        Args:
            value: width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # property decorator to retrieve height
    @property
    def height(self):
        """height getter method
        """
        return self.__height

    # property decorator to set height
    @height.setter
    def height(self, value):
        """height setter method
        Args:
            value: height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
