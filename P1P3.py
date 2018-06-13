nihi# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:34:27 2017

@author: Nikhil Bansal

* Objective : Find longest string in incresing alphabetic order
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
str = input("type : ")

#check and reprompt if user enter empty string
while len(str) <= 0:
    print("Please enter valid string")
    str = input("type : ")

# result = longest string in alphabetic order
# ss =  temp. intermediate result in process    
# pr = contain position of char in alphabet string, used to decide order
result = str[0]
pr = alphabet.index(str[0])
ss = result

#traversing input string 
for c in str[1:]:
    
    #check if next char is in alphabetically increasing order than previous
    if(alphabet.index(c) >= pr):
        #if yes - update temp. result and ordring position 
        ss = ss + c
        pr = alphabet.index(c)
        print("S", c, ss, pr, result)
    else:
        #if no - update result, temp. resilt and ordring position
        if(len(ss) > len(result)):
            result = ss
        ss = c
        pr = alphabet.index(c)

if(len(ss) > len(result)):
            result = ss
print(result)