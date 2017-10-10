# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:56:22 2017

@author: a0564671
"""

s=str(input("Enter String: "))

letters= "abcdefghijklmnopqrstuvwxyz"
key="1002140719061812070817001907141814191300010200"
key_count=0
for letter in s:
    ltr_nbr=0
    if letter !=" ":
        for each in letters:
            ltr_nbr+=1
            if letter == each:
                keyrec=""
                if key_count%2 == 0:
                    keyrec=key[key_count:(2+key_count)]
                else:
                    keyrec=key[(key_count+1):(3+key_count)]
                
                    Ukbn Txltbz nal hh Uoxelmgox wdvg Akw; hvu ogl rsm ar sbv ix jwz
