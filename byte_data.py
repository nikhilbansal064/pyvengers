# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 23:05:20 2018

@author: Nikhil Bansal

* byte form of data is used when ever we want to transfer data through network or store data in files.
* "struct" module is used to convert data to byte form and  vice versa

"""

"""
Captain America (during civil war) want to send data to falcon. data is day, month and other
details of attack on Iron man. Since tony was tracking all their convertation , captain decide to
send data in byte form and now ...

"""
from struct import *


encrypted_data = pack('iif', 2, 4, 2.02)
# he send encrypted data to falcon
print(encrypted_data) 


# methos to calcute size aquired by each format
print(calcsize("i"))


#here falcon is dycrypting it
msg = unpack('iif', encrypted_data)
print(msg)