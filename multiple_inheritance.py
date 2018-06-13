# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:05:35 2018

@author: Nikhil Bansal

 * multiple inheritance - In python a class can inherite form multiple classes
 * Diamond problem - solution  - mro(method resolution order) i.e depth forst and left to right.
 
"""

class Man:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
        
class Suit:
    def __init__(self, type):
        self.type = type
    
    def get_name(self):
        return self.type
    
    def get_type(self):
        return self.type
        

#Here comes the multiple inheritance
# just change order of parenr class and u will see the difference in method resolution.
class Suited_man(Suit, Man):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def get_id(self):
        print("Hey I am " + self.get_name() + " and I am " + self.get_type() + "man")


iron_man = Suited_man("Tony", "iron")
iron_man.get_id()
