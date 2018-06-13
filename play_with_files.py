# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:04:48 2018

@author: Nikhil Bansal

 - Python deals two type of files:
     1. Text files - Data stored in text and each line ends with EOL(End of line)
                     '\n' is default EOL in python
    
     2. Binary Files - Data stored in binaries (0 nad 1), no EOL
     
 - Access modes - we can open text files in different access modes:
     1. "r" - Read, Cursor at begining of file and I/O error if file not exists
     2. "r+" - Read + Write, Cursor at begining of file and I/O error if file not exists
     
     3. "w" = Write, Cursor at begining of file and create new if file not exists, override content of existing files
     4. "w+" = Read + Write, Cursor at begining of file and create new if file not exists, override content of existing files
     
     5. "a" = Write, Cursor at end of file and create new if file not exists, append if existing files
     6. "a+" = Read + Write, Cursor at begining of file and create new if file not exists, append if existing files
     
 - close() - close file and release space used by it. When file no longer needed, close it
"""

# Hi I Scarlet witch. I'm gonna write in my feeling in my diary today. Shh.. its a scerate
diary_write = open("Wands's Diary.txt", "w+")
diary_write.write("I love Captain America, He  is so Handsome (Blush)")
# Ohh some one is coming,I should go now
diary_write.close()

# Hi I Vision.Today we gonna read wanda's diary. I know she loves me. lets see

#diary_append = open("Scarlet's Diary.txt", "r") - give error as this file dont exist
diary_read = open("Wands's Diary.txt", "r+")
wandas_secrete = diary_read.read()
#You wanna see it??
print(wandas_secrete)
print("Vision: (Weep) Thanos, kill me please (more weep and moan)")

# Hi I am captain america. Vision is going mad> I have to handle situation
diary_append = open("Wands's Diary.txt", "a+")
diary_append.write(". But Vision is love of my life.")
diary_append.close() 
print("captain: Vision please look at diary again?")

# Hi I Vision. Only for you captain
diary_read = open("Wands's Diary.txt", "r+")
wandas_secrete = diary_read.read()
#You wanna see it??
print(wandas_secrete)
print("Vision: I was fool, Wanda I love you too, Thanks captain.")

print("Captain: What a stupid.")




 

