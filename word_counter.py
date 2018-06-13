# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:13:45 2018

@author: Nikhil Bansal

Here we are going to create a word counter.
* steps - 1. We are gointn to screap a web page to get words.
"""

import requests
from bs4 import BeautifulSoup
import re
import operator


# This method is going to give us word list
def get_words(url):
    
    word_list = []
    
    # get whole html code in text format in source_code
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    
    # find all titles in source code
    for line in soup.findAll("a", {"class" : "cellMainLink"}):
        
        # strip html code form line
        title = line.string
        
        # used re(regex) module to split title with multiple delimeters.
        # use escape character with "."
        words = re.split('-|\.', title.lower())
        word_list.extend(words)
    
    
    return word_list
    

# This method will take word list and return dictionary with words and their frequency.
def calculate_freq(words):
    freq_table = {}
    
    #check if word is already in dictonary
    for word in words:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
            
    
    #sort dictonary according to key
    sorted_table = sorted(freq_table.items(),key=operator.itemgetter(0))
    
    return sorted_table
    
url = "https://kickass.unblocked.lat/tv/"
word_count = calculate_freq(get_words(url))

#display word count
for key, value in word_count:
    print(key, value)