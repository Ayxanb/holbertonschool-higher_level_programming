#!/usr/bin/python3

''' I hate writing docstr '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' I hate writing docstr '''
    def __init__(self, size):
        ''' I hate writing docstr '''
        self.integer_validator('size', size)

        self.__size = size

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
