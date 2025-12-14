#!/usr/bin/python3

''' I hate writing docstr '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    ''' I hate writing docstr '''
    def __init__(self, width, height):
        ''' I hate writing docstr '''
        integer_validator('width', width)
        integer_validator('height', height)

        self.__width = width
        self.__height = height
