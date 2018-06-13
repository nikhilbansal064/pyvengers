# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:25:46 2017

@author: Nikhil Bansal
"""

def selectionSort(list):
    l = len(list)
    suffixSt = 0
    
    while suffixSt < l:
        print(list)
        for i in range(suffixSt, l):
            if(list[i] < list[suffixSt]):
                temp = list[i]
                list[i] = list[suffixSt]
                list[suffixSt] = temp
        
        suffixSt += 1
    
    return list


list = [9,4,6,5,3,8]
print(selectionSort(list))