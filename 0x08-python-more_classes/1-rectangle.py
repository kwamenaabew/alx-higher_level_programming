#!/usr/bin/python3

class Rectangle:
    """
    Empty class that defines a rectangle

    Attribute: None
    """
    def __init__(self, width=0, height=0):
        """
        Init method for Class Rectangle
        Attributes:
        w: width of the rectangle
        h: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property width to get the width
        Returns:
        width (int) : The width of the class Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width of the Rectangle
        Attributes:
        width: The width  of the Rectangle
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
            """
            Property height to get the height
            Returns:
            height (int) : The width of the Rectangle
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter for height of the Rectangle
            Attributes:
            height: The height of the Rectangle
            Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >=0")
            else:
                self.__height = value
