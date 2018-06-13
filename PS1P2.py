# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:10:28 2017

@author: Nikhil Bansal
"""
count = 0
s = input("enter string : ")
i = 0
state = 0
while i < (len(s)):
    if s[i] == "b":
        if state == 0:
            state = 1
        if state == 2:
            count += 1
            state = 1
    elif s[i] == "o":
        if state == 1:
            state = 2
        else:
            state = 0
    i += 1
print(count)
                
    