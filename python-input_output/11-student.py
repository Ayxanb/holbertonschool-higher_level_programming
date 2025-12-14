#!/usr/bin/python3
"""I hate docstring"""


class Student:
    """I hate docstring"""

    def __init__(self, first_name, last_name, age):
        """I hate docstring"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """I hate docstring"""
        if isinstance(attrs, list):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """I hate docstring"""
        for key, value in json.items():
            setattr(self, key, value)
