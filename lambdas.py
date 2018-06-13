# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:07:35 2018

@author: Nikhil Bansal

* lambdas - small anonymous function i.e function with no name. 
          - syntax : lambda arg: exp
          - only single expression is allowed.

* Use - create funtion for one time use.
      - use with filter(), map(), reduce() built in methods.
      
"""
import functools
# example 1
incrementor = lambda x: x + 1
print(incrementor(5))

# example 2 - use with built in function

l = [1,2,3,4,5,6,7,9,10]
# 1. filter(function, list)
nl = filter(lambda x: x%2 == 0, l)
print(list(nl))

# 1. map(function, list)
nl = map(lambda x: x*2, l)
print(list(nl))

# 1. reduce(function, list)
#reduce is not working
sum = functools.reduce(lambda x, x1: x + x1, l)
print(sum)


