# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:00:56 2018

@author: Nikhil Bansal

 - Reverse of packing of args( or var_args i.e *args)
 - Use - When we want to map function args with list values
 - No. of args must be equal to list size
"""

def unpacking_gifts(g1, g2, g3):
    print("Yeah I have got %s, %s and %s" %(g1, g2, g3))
    

gift_list = ["Teddy", "Choclates", "Dresses"]

# passing argumens like this is very tedious 
unpacking_gifts(gift_list[0], gift_list[1], gift_list[2])

#Voila! we can unpack gift_list
unpacking_gifts(*gift_list)

# but we have to take care for no. of arge passed
gift_list.append("Cards")
unpacking_gifts(*gift_list)
