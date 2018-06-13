# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:56:59 2017

@author: Nikhil Bansal
"""
def printMove(to, fr, file):
    """
       input : fr - initial tower
               to - destnatin tower
               
       fun : print move of TowerOfH
    """
    file.write("Move from " + fr + " to " +  to)
def towerOfH(n, fr, to, spare, file):
    """
        input : n - int, no. of disks
                to - string, destination tower
                from - string, initial tower
                spare - string, spare tower for help
    """
    #base case
    if(n == 1):
        printMove(fr, to, file)
    
    towerOfH(n - 1, fr, spare, to, file)
    towerOfH(1, fr, to, spare, file)
    towerOfH(n - 1, spare, to, file)
    
# file to save result
towerHandle = open("toh.txt", "w")
towerOfH(2, "T1", "T2", "T3", towerHandle)
towerHandle.close()