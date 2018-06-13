# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:37:06 2017

@author: Nikhil Bansal
"""
    
def applyF_filterG(L, f, g):
    """
        input : 1. List of integers
                2. f - function, return an integer 
                3. g - funtction, return boolean
    """
    
    # Base case
    if(len(L) == 0):
        return -1
    #clone of list to avoid side effect due to mutation
    tempList = L[:]
    
    # iteration each element over list
    for e in tempList:
        # check for element type , raise exception element is not integer
        assert (type(e) is int), "list elements are not integers"
        # result after applying given 2 function on list element
        result = g(f(e))
        
        # if result is not True , remove element from temp list.
        #(Caution- removing element from original list can cause side effectes)
        if(not result):
            L.remove(e)
        
    #Check if list is empty
    if(len(L) == 0):
        return -1
          
    #sort resulted list
    #L.sort()
    # return largest element
    return sorted(L)[-1]

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 6,5, -4]
print(applyF_filterG(L, f, g))
print(L)
        