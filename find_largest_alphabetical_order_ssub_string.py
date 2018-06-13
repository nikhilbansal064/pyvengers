# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:09:17 2018

@author: Nikhil Bansal

* Objective : Find longest string in incresing alphabetic order

"""

#check and reprompt if user enter empty string
str = input("Enter input String please -  : ")
while len(str) <= 0:
    print("Please enter valid string")
    str = input("Enter input String please -  : ").lower()
    

result = str[0]
temp_result = str[0]
l = len(str)

for i in range(1 , l):
   
    #print("temp - %s , result - %s, curr char %s, pre char - %s" %(temp_result, result, str[i], str[p]))
    if(str[i] >= str[i - 1]):
        temp_result += str[i]
    elif(len(temp_result) > len(result)):
        result = temp_result
        temp_result = str[i]
    else:
        temp_result = str[i]
        
    #check if remaining char are less than current result lenth then leave calculation
    if(len(result) >= (len(temp_result) + l - i)):
        break
    
# finally get result    
if(len(temp_result) > len(result)):
    result = temp_result
        

print(result)