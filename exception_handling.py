# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:03:33 2018

@author: Nikhil Bansal

 * Exception  - Error that occure at runtime
 * we use - try...except...finally  construct to handle exception
 * try - put suspecting code in try clause
 * except - handler code for goes here
* finally - code here will execute in any case 

"""
#This code will give exception on wrong answer
stones = int(input("How many stones Thanos have?\n"))
print(5/stones)

# I will continue to interrogate untill you will give me right answer
# Let me handle all your dirty exceptions

while True:
    try:    
        stones = int(input("How many stones Thanos have?\n"))
        print(5/stones)
        break
    except ValueError:
        print("Give me proper count.\n")
    except ZeroDivisionError:
        print("Dont u dare to say 0 again, I know he have more than zero stones.")
    except:
        print("What!! you are Groot! ")
    finally:
        print("Buckle up fellas!. we need to stop thanos.")
    
