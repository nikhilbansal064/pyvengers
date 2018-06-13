# -*- coding: utf-8 -*-
"""
Created on sunday June  3 21:18:01 2018

@author: Nikhil Bansal

 - Inheritance - passing properties and behaviour from one class to another. Parent class -> Child class
 - attribute resolution in Child class - If searched attribute is not found in Child class then the search proceeds to
                                         it's Parent class and so on.
 - Child class can override Parent class's method
 - Useful built in functions for inheritance - 1. isinstance(obj, c1) : True if obj is instance of class c1 or of any of
                                                  it's child class.

                                               2. issubclass(c1, c2) : True if c1 is subclass id c2
"""


class Parent:
    # class variable
    lastname = "Bansal"

    def get_last_name(self):
        print(self.lastname)


class Child(Parent):

    def __init__(self, name):
        self.firstname = name

    def get_first_name(self):
        print(self.firstname)

nikhil = Child("nikhil")
nikhil.get_first_name()
nikhil.get_last_name()
print(isinstance(nikhil, Parent))
print(issubclass(Child, Parent))
