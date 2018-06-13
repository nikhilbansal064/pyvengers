# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:14:51 2018

@author: Nikhil Bansal
"""

text = "Free online courses from Massachusetts Institute of Technology\
        Massachusetts Institute of Technology — a coeducational, privately \
        endowed research university founded in 1861 — is dedicated to advancing\
        knowledge and educating students in science, technology, and other areas \
        of scholarship that will best serve the nation and the world in the \
        21st century. Learn more about MIT. Through MITx, the Institute furthers \
        its commitment to improving education worldwide."
        
 
from collections import Counter       
word_list = text.split()
counter = Counter(word_list)
print(counter.most_common(3))
print(counter)