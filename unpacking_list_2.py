# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:49:38 2018

@author: Nikhil 

* Objective - we can unpack the list in various ways
"""
#one example 

# suppose we have list that contains person name and its secrete identity.
avenger = ["Scott lang", "Ant man"]

#One way to do it
name = avenger[0]
id = avenger[1]
print(name + " is " +  id)

#better way to do it, called unpacking of list 
name, id = avenger
print(name + " is " + id) 




#another story

"""
Doctor strange and wand fooled guardians by saying them that they can make then invisible.
Now...

"""
 
squad = ["Doctor strange", "Star lord", "Gamora", "Groot", "Rocket", "Wanda"]

#unpacking
fornt_magician, *fools, last_magician = squad

# U wanna know who the fools are
print("these are fools")
for fool in fools:
    print(fool)



