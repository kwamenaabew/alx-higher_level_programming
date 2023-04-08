#!/usr/bin/python3
"""
class rectangle that defines a rectangle by: (based on 3-rectangle.py)

"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """init method with private instance attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method
        Returns:   width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter method
        Args:
            value: width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method
        Returns:   height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter method
        Args:
            value: height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    #instantiation with optional width and height: def __init__(self, width=0, height=0):
    def area(self):
        """area method
        Returns:   area of rectangle width * height
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """perimeter method
        Returns:   perimeter of rectangle width + width + height + height
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
    
    #print() and str() should print the rectangle with the character #: (see example below)
    #if width or height is equal to 0, return an empty string
    def __str__(self):
        """str method
        Returns:   rectangle with the character #
        """
        strng = ""
        if self.__width == 0 or self.__height == 0:
            return strng
        
        for i in range(self.__height):
            for j in range(self.__width):
                strng += "#"
            if i < self.__height - 1:
                strng += "#"
        return strng
    
    #repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval(): (see example below)
    def __repr__(self):
        """repr method
        Returns:   string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)