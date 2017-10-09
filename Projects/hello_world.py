# -*- coding: utf-8 -*-
"""
Created on 10.6.17
Author: Cody Schierbaum
"""

print("hello world")
print("I like 6.00.1x!")

x = int(input("Enter an intiger: "))
ans =0
while ans**3 < x:
    ans +=1
if ans**3 != x:
    print(str(x) + " is not a perfect cube.")
else:
    print("Cube root of " + str(x) + " is " + str(ans))
    