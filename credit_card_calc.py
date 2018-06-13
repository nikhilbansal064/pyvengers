# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:38:32 2017

@author: Nikhil Bansal
"""

def ccDebt(balance, annualIntrestRate, monthlyPaymentrate):
    
    amtToPay = balance
    for i in range(12):
        monthlypayment = round(amtToPay * (monthlyPaymentrate), 2)
        amtToPay = round((amtToPay - monthlypayment) *(1 + (annualIntrestRate / 12)), 2)
        
    return ("Remaining Balance : " + str(round(amtToPay, 2)))
    
ccDebt(42,0.2,0.04)