# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:34:59 2017

@author: Nikhil Bansal
"""

def strPlay(puzzle):
    
    """
        input : string after doing binary search procedure
        output : original string
        approach : sience each successive letter in puzzel is the center letter of original str
                   we will take letters form puzzel and append them in origianl str in front then in 
                   last, alternativly.
    """
    
    length = len(puzzle)
    #keep tract , where to append letter form puzzel to original str(start or end)  
    toRight = False
    originalStr = ""
    
    #if len is even, i.e 2nd letter in puzzle will be in right of 1 letter in original str
    if(length % 2 == 0):
        toRight = True
    else:
        toRight = False
        
    originalStr += puzzle[0]
    
    for c in puzzle[1:]:
        if(toRight):
            originalStr = originalStr + c
        else:
            originalStr = c + originalStr
            
        toRight = not(toRight)
    print(originalStr)
    

p = "khiinl"
strPlay(p)