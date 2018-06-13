# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:50:58 2017

@author: Nikhil Bansal
"""

def isIn(char, aStr):
    """
    input : 1. char - charachter type
            2. aStr - String type (str in alphabetical order)
            
    output : boolean
    
    fun : using bisection search to find char in giver str
    """
    if(char == ""):
        return False
    
    if(len(aStr) == 0):
        return False
    
    if(len(aStr) == 1):
        if(char == aStr[0]):
            return True
        else:
            return False
        
    mid = int(len(aStr) / 2)    
    if(aStr[mid] == char):
        return True
    else:
        if(aStr[mid] < char):
            return isIn(char, aStr[mid + 1:])
        else:
            return isIn(char, aStr[:mid])

i = isIn('c', 'cfhjnxz')
print(i)    
    
    