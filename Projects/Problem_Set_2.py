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
step=0
while step<char_count-2:
    bob_test=s[step]+s[step+1]+s[step+2]
    if bob_test=="bob":
        bob_count+=1
    step+=1
print(bob_count)
