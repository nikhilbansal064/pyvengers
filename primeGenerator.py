# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:31:51 2017

@author: Nikhil Bansal
"""
import math
def genPrimes():
    n = 2
    
    while True:
        if(isPrime(n)):
            yield n
        n += 1

def isPrime(n):
    prime = True
    if(n == 2):
        prime = True
        return prime
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if(n % i == 0):
            prime = False
            break
    return prime

p = genPrimes()
for i in range(10):
    print(next(p))