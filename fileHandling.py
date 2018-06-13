# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:32:31 2017

@author: Nikhil Bansal
"""

"""
A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

"""
def writeInFile(file, content):
    
    circleHandle = open(file, "w")
    
    for i in range(2):
        circleHandle.write(content + "\n")
        
    circleHandle.write("Bye")
    circleHandle.write("dfdgddgdgdgdgdgdg" + "\n")
    circleHandle.close()
    
writeInFile("circle", "this is circle file")