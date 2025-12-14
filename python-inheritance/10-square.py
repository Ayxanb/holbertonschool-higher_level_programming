#!/usr/bin/python3

''' I hate writing docstr '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' I hate writing docstr '''
    def __init__(self, size):
        ''' I hate writing docstr '''
        self.integer_validator('size', size)

        super().__init__(self, size, size)
