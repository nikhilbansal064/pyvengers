# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:03:39 2018

@author: Nikhil Bansal
"""
import random
import urllib.request

def download_image(image_url):
    #we need to give a name to image
    name = "img" + str(random.randrange(1, 1000)) + ".jpeg"

    
    #This is magic line! hell yeah!!
    urllib.request.urlretrieve(image_url, name)
    
    #lets celebrate
    print("Task done.Boom")
    

def download_pdf(pdf_url):
    name = "pdf" + str(random.randrange(1, 1000)) + ".pdf"
    #This is magic line! hell yeah!!
    urllib.request.urlretrieve(pdf_url, name)
    
    #lets celebrate
    print("Task done.Boom")

#Can we download image? Sure lets see
img_url = "http://icons.iconarchive.com/icons/graphicloads/100-flat-2/256/arrow-download-icon.png"
pdf_url = "http://www.shreeramgroup.com/pdf/umang.pdf"
video_url = "https://www.youtube.com/watch?v=MjwWzBiAMck&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=23"
download_image(img_url)

# Yes, we can download any type of file. Lest try pdf
download_pdf(pdf_url)