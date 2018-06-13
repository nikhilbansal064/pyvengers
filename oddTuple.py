# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:19:37 2017

@author: Nikhil Bansal
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    i = 0
    outTup = ()
    while i < len(aTup):
        outTup = outTup + (aTup[i],)
        i +=2
        
    return outTup

t = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(t))
