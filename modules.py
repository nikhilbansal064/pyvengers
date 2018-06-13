# -*- coding: utf-8 -*-
import random 
import avengers_helpline

"""
Created on Tue May  8 22:58:43 2018

@author: Nikhil Bansal

* Module - A python file which contain python code 
         - Generally contains function, which are going to be resued by other python files
* Use - Modularity in programs and reusability of code
* Importing module must be the first lines of program
"""
vilian_list = ["loki", "thanos", "ultron", "hydra"]


def take_counter_attack():
    # Coz Hulk fears thanos
    attacker = vilian_list[random.randint(0, len(vilian_list) - 1)]
    if(attacker == "thanos"):
        print("We need to call Iron Man ASAP")
        
    while attacker != "thanos":
        print("Ohh! for you %s we have %s" %(attacker, avengers_helpline.attack_hulk()))
        attacker = vilian_list[random.randint(0, len(vilian_list) - 1)]
        

print("Earth is Under attack, Please Help!!")
take_counter_attack()       



        