# -*- codi:""ng: utf-8 -*-
"""
Created on Wed Oct 11 22:30:40 2017

@author: Nikhil Bansal
"""
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Base case
    if(N <= 0):
        return 0
    
    return (N % 10) + sumDigits(N // 10)

print(sumDigits())

 