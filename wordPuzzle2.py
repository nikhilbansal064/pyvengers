# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:20:08 2017

@author: Nikhil Bansal
"""

    
    
def wordPuzzel(s, k):
    """
    input:
        s : constans String
        k : no of minimum consonents which are required to be in string 
        
    output:
        minLen : minimum length of all substring which contain minimum k consonents
        
    """
    consonants = "bcdfghjklmnpqrstvwxyz"
    strLen = len(s)
    #number_of_consonants = sum(word.count(c) for c in consonants)
    sLower = s.lower()
    for l in range(k , strLen):
        subStrsList = [sLower[i:i + l] for i in range(strLen - l + 1)]
        print(subStrsList)
        found = True
        for ss in subStrsList:
            conCount = sum(ss.count(c) for c in consonants)
            
            if(conCount < k):
                found = False
                break
        
        if(found):
            return l
        else:
            continue
    
    return -1


s = "ritikisagoodboy"
k = 4
ans = wordPuzzel(s, k)
print(ans)