# -*- coding: utf-8 -*-
import random
"""
Created on Mon May  7 23:24:55 2018

@author: Nikhil Bansal
"""

def sayHello(name):
    print("Hello %s !!" %(name))
    
def bitcoin_to_usd(btc):
    return btc*527

def dating_age(age = 12):
    return (age / 2) + 7

rand_num = random.randrange(0,25)

def get_sex(sex = 'u'):
    if sex == 'm':
        print("Male")
    elif sex == 'f':
        print("Female")
    else:
        print("Unknown")
        
get_sex('f')
get_sex('m')
get_sex()
get_sex("ds")