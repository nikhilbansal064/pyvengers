# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:34:31 2017

@author: Nikhil Bansal

Here we will define 2 methods to calculate fibonacci number.
one with using dict. , which is efficient and use memoization technique
while other is simple one and inefficient
"""
#simple fib calculator
"""
    input - n, int type
    output - fib no. corresponding to n

"""
def fib(n):
    #with use of "global" keywords we can access and modify the global variable
    #by default we can only access it but cant modify it
    global count
    count += 1
    
    #Base cases
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    
    return fib(n -1 ) + fib (n - 2)

#efficient fib calculator
"""
    input - n, int type
            d, dictonary. to store already calculated fib values
            
    output - fib no. corresponding to n
"""
def eff_fib(n, d):
    global count
    count += 1
    
    #check if fib is already in d
    if(n in d.keys()):
        return d[n]
    else:
        ans = eff_fib(n - 1, d)  +  eff_fib(n - 2, d)
        d[n] = ans
        return ans


d = {1:1, 2:2}
n = 30
count = 0
print("normal fib of ", n, " is =", fib(n), "in steps =", count)
count = 0
print("efficient fib of ", n, " is =", eff_fib(n, d), "in steps =", count)    