#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 3

Created on Mon Oct  9 22:37:07 2017

@author: Cody Schierbaum
"""

s= str(input("enter a string: "))
letter_value = "abcdefghijklmnopqrstuvwxyz"
s_length=0
test_str_1=""
test_str_2=""
test_val=0
len_1=0
len_2=0
for letter in s:
    s_length+=1
    
for letter in range (s_length):
    for test in range(26):
        if s[letter] == letter_value[test]:
         if test_val<=test:
             test_val=test
             test_str_1= test_str_1 + letter_value[test]
             len_1+=1
         elif test_val>test:
             if len_1>len_2: 
                 len_2=len_1
                 test_val=test
                 test_str_2=test_str_1
                 test_str_1=""
                 test_str_1= test_str_1 + letter_value[test]
                 len_1=1
             else:
                 len_1=1
                 test_val=test
                 test_str_1=""
                 test_str_1= test_str_1 + letter_value[test]
                 
if test_str_2 !="":
    if len_2>=len_1:
        print(test_str_2)
    else:
         print(test_str_1)
else:
    print(test_str_1)