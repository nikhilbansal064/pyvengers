# -*- coding: utf-8 -*-

count = 0
s = input("Enter some string : ")
for c in s:
    if((c == "a") or (c == "e") or (c == "i") or (c == "o") or (c == "u")):
        count += 1
print(count)
        
    