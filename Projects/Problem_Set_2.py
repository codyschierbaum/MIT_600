# -*- coding: utf-8 -*-
"""
Problem set 2

Created on Mon Oct  9 16:24:46 2017

@author: Cody Schierbaum
"""

s = str(input("Enter a string: "))

bob_count=0
bob_test=""
char_count =0
for letter in s :
    char_count+=1
while char_count-2>=0:
    bob_test=s[char_count-3]+s[char_count-2]+s[char_count-1]
    if bob_test=="bob":
        bob_count+=1
    char_count-=1
print(bob_count)
