# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:15:31 2018

@author: Nikhil Bansal

 * Set - collection of items but
            - No orderered is mainteained
            - No duplicates
            - only accept hashable(immutable) elements i.e list cant be element of set
            - base on hashtable
            
 * Use - better than list, if we want to check availability of element on collection 
"""

# we can make set by passing iterable
avengers_iterable = ["Iron Man", "Thor", "Captian America", "Iron Man"]
avenger_set = set(avengers_iterable)

# yes we can make set this way also
gurdians_set = {"Star Lord", "Groot", "Roket" "Drax","gamora", "nebula", "Thor"}

alien_set = {"Star Lord", "Groot", "Roket" "Drax","gamora", "nebula", "Thor", "Loki"}

#this line here gives error, cause set only accept immutalbe/ hashable elements but list
# is mutable
#gurdians = {"Star Lord", "Groot", "Roket" "Drax", ["gamora", "nebula"]}


print(avenger_set)
print(gurdians_set)

#yeah!! I ganna make a big team
print(avenger_set | alien_set)

# Thor is every where
print(avenger_set & alien_set)
