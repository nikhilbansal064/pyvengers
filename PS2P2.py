# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:45:42 2017

@author: Nikhil Bansal
"""

def calcFixAmt(balance, annualInterestRate):
    
    #initialise upper bounds and lower bounds for bisection search
    monthlyInterestRate = annualInterestRate / 12
    start = balance / 12
    end = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
    fixAmt = (start + end) / 2 
    found = False
    
    while True:
        
        amtToPay = balance
        fixAmt = (start + end) / 2
        
        #loop to calc amt to pay by calculating unpaid balance each month
        for i in range(12):
            unpaidBal = amtToPay - fixAmt;
            amtToPay = unpaidBal * (1 + (annualInterestRate / 12))
            
        
        #check for right result
        if(abs(amtToPay - 0) <= 0.01):
            found = True
            break
        else:
            # update bounds
            found = False
            if(amtToPay < 0):
                end = fixAmt
            else:
                start = fixAmt
        
    if(found == True):
        print("Fix amt = ", round(fixAmt, 2))
        
calcFixAmt(320000, 0.2)        
                
        
        
