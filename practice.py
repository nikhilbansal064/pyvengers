# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:34:27 2017

@author: Nikhil Bansal
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
str = input("type : ")

while len(str) <= 0:
    print("Please enter valid string")
    str = input("type : ")
    
result = str[0]
pr = alphabet.index(str[0])
ss = result

print(pr, result, ss)
for c in str[1:]:
    print(c, alphabet.index(c), pr)
    if(alphabet.index(c) >= pr):
        ss = ss + c
        pr = alphabet.index(c)
        print("S", c, ss, pr, result)
    else:
        if(len(ss) > len(result)):
            print("F : changing result with ss", result, ss)
            result = ss
        ss = c
        pr = alphabet.index(c)
        print("F", c, ss, pr, result)

if(len(ss) > len(result)):
            result = ss
print(result)