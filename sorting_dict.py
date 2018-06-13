# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:36:48 2018

@author: Nikhil Bansal

* There is not buildt funvtion in python for sorting of dictonary. Because by nature 
    dictonary is un ordered and used for fast lookup.
    
* There are some methods - 1. sorted funtion 
                           2. zip() 
                
"""

avengers_power = {"Iron man" : 99, 
                  "Hulk" : 159,
                  "doctor strange" : 123,
                  "Captain america" : 97,
                  "Vision" : 122}

# suppose we wanted to sort this dict, power(i.e value) wise

# 1. We can zip dictonary. since Zip function give sorted list of tuples, which can be sorted
#    based on first list given.
print(sorted(zip(avengers_power.values(), avengers_power.keys())))

# 2. we can use operator
import operator
# sort based on keys
print(sorted(avengers_power.items(), key=operator.itemgetter(0)))

# sort based on keys
print(sorted(avengers_power.items(), key=operator.itemgetter(1)))

# 3. we can use lambda
print(sorted(avengers_power.items(), key= lambda item: item[0]))
print(sorted(avengers_power.items(), key= lambda item: item[1]))

