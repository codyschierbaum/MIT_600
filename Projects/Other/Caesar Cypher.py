#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caesar Cypher Tool

Created on Tue Oct 10 19:32:11 2017

@author: cody
"""

EorD = str(input("Encrypt or Decrypt:"))
alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[]\:;',>./`1234567890-|= "
dout=""
if EorD == "decrypt":
    #Decryption
    
    Dstr=str(input("Enter message to decrypt:"))
    shift=str(input("Enter shift:"))
    
    if shift != "":
        shift=1+int(shift)
        for letter in Dstr:
            if letter!="":
                kcount=0
                for k in alpha:
                    kcount+=1
                    if letter == k:
                        dout+=alpha[kcount-shift]
            else:
                dout+=letter
        print(dout)
    else:
        for shift in range(1,28) :
            for letter in Dstr:
                if letter!=" ":
                    kcount=0
                    for k in alpha:
                        kcount+=1
                        if letter == k:
                            dout+=alpha[kcount-shift]
                else:
                    dout+=letter
            print(str(shift-1) + ": " + dout)
            dout=""
            
            
else:
    Dstr=str(input("Enter message to encrypt:"))
    shift=int(input("Enter shift:"))-1
    for letter in Dstr:
        if letter!=" ":
            kcount=0
            for k in alpha:
                kcount+=1
                if letter == k:
                    dout+=alpha[kcount+shift]
        else:
            dout+=letter       
    print(dout)
     