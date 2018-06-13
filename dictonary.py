# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:42:58 2018

@author: Nikhil Bansal

* Dictonary - similar to map
            - have key, value pairs 
"""

#this will create an empty dict
avengers_ids = dict()
avengers_ids["Iron Man"] = "Tony Stark"
avengers_ids["Spider Man"] = "Peter parker"
avengers_ids["Black Panther"] = "T'Chala"
avengers_ids["Hulk"] = "Bruce"

# You could have use this easy method to make dict
gurdians_ids = {"Star Lord" : "Peter Quill", "Gamora" : "Green girl"}

# Ohh, You are so cool
print("You know Iron man is ", avengers_ids["Iron Man"])

# Now you are boasting...Really
for name, id in gurdians_ids.items():
    print("And %s is %s" %(name, id))

