#!/usr/bin/python3

''' I hate docstring '''

import pickle

class CustomObject:
    ''' I hate docstring '''


    def __init__(self, name, age, is_student):
        ''' I hate docstring '''
        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        ''' I hate docstring '''
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")


    def serialize(self, filename):
        ''' I hate docstring '''
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        ''' I hate docstring '''

        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            return None
