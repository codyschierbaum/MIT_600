# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:06:42 2017

@author: a0564671
"""

#calculates the minimum payment given minimum payment rate and current balance
def PmtAmt(PmtRate,Bal):
        return(PmtRate*Bal)

#calculates remaining balance given current balance and payment made
def RemainBal(Bal,Pmt):
    return(Bal-Pmt)

#calculates the interest charged for a given balance at a given rate
def IntAmt(rate,Bal):
    return(rate/12)*Bal
    
def MonBal(balance,payment,interest):
    balance=RemainBal(balance,PmtAmt(payment,balance))
    return balance +IntAmt(interest,balance)

def MonBalFxd(balance,payment,interest):
    balance=RemainBal(balance,payment)
    return balance +IntAmt(interest,balance)

def Yr_Pmt(balance,annualInterestRate,monthlyPaymentRate):
    for month in range(0,12):
        balance=MonBal(balance,monthlyPaymentRate ,annualInterestRate)
        month+=1
    return round(balance,2)

def Yr_PmtFxd(balance,annualInterestRate,monthlyPaymentRate):
    for month in range(0,12):
        balance=MonBalFxd(balance,monthlyPaymentRate ,annualInterestRate)
        month+=1
    return round(balance,2)

def PmtSrch(bal,intr):
    mplb=bal/12
    mpub=bal*(1+intr)/12
    mp=(mpub+mplb)/2
    test=Yr_PmtFxd(bal,intr,mp)
    while test!=0:
        if test<0:          
            mpub=mp
            mp=(mpub+mplb)/2
            test=Yr_PmtFxd(bal,intr,mp)
        elif test>0:
            mplb=mp
            mp=(mpub+mplb)/2
            test=Yr_PmtFxd(bal,intr,mp)
    return(round(mp,2))

