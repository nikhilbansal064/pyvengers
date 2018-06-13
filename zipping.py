# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:22:18 2018

@author: Nikhil Bansal

* Zip(l1, l2, l3)/ zip(*iterators) - This method is used to map similar index of different containers(l1, l2, l3)
                    so that they can used as single entity.
                  
                 - It actually make list of tupels as [(l[0], l[1], l[2]), ......]

* Use - to collect the saperated info
                    
"""

# some stupid kids are discussing about avengers and their power score
# First says I have list of avengers
heros = ["Iron Man","Ant Man", "Spider Man"]

# Second says I know their real names
names = ["Tony stark","Scott lang", "Peter park"]

# Third says I know their power score
scores = ["99","59", "78"]

# But these different list are hard to manage, I wanted more formated info. hmm...
# Suddenly I found zip()
hero_info = zip(heros,names, scores)

#Now see the magic
print(type(hero_info))
for hero, name, score in hero_info:
    print("%s - %s - %s" %(hero, name, score))


#Hold on we can unzip also
# h, n, s = zip(*zip(heros,names, scores) - will throw type error
h, n, s = zip(*zip(heros,names, scores)
)
print(h)
print(n)
print(s)