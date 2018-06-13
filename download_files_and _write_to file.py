# -*- coding: utf-8 -*-'
from urllib import request
"""
Created on Thu May 10 22:59:43 2018

@author: Nikhil Bansal


"""

def download_file(url):
    response = request.urlopen(url)
    data = str(response.read())
    formatted_data = data.split("\n")
    
    
    dest_file = open("data_dest.txt", "w+")
    for line in formatted_data:
        dest_file.write(data + "KAAABOOOOMMMMMMM")
        
    dest_file.close()
    print("Boom")
    
    

file_url = "https://www.google.com/finance/getprices?q=GOOGL&i=60&p=1d&f=d,c,v,o,h,l"
download_file(file_url)
