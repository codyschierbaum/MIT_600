# -*- coding: utf-8 -*-
"""
Problem set 1

Created on Mon Oct  9 16:24:47 2017

@author: Cody Schierbaum
"""

s= str(input("Enter a string: "))
vowels=0

for letter in s:
    if letter =="a" or letter == "e" or letter == "i" or letter == "o" or \
    letter =="u":
        vowels+=1
    
print("Number of vowels: " + str(vowels))
    