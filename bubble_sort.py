# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:01:17 2017

@author: Nikhil Bansal
"""

def bubbleSort(list):
    l = len(list)
    swap = False
    
    while not swap:
        print(list)
        swap = True
        for i in range(l - 1):
            if(list[i] > list[i + 1]):
                swap = False
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                
                
    return list


list = [2,3,5,9,4,3,8]
print(bubbleSort(list))