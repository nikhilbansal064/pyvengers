# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:18:01 2018

@author: Nikhil Bansal

 - var_args - we can pass variable no. of argument in python function(even zero no. of arguments)
 - Using the *, the variable that we associate with the * becomes an iterable, meaning you 
   can do things like iterate over it,run some higher order functions such as map and filter.
 - *args == here args is a tuple 

 - This is also called packing of arguments, as we are packing diff. no of arguments in a single
   variable.
   
 - Use - when no. of arguments are variable  
"""


def multiply(*args):
    tot = 1
    for arg in args:
        tot *= arg
    print(tot)


multiply(2, 38, 3, 365, 322, 545, 0)
multiply()
