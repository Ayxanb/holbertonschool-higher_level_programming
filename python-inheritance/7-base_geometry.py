#!/usr/bin/python3
"""I hate docstring"""


class BaseGeometry:
    """I hate docstring"""

    def area(self):
        """I hate docstring"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """I hate docstring"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
