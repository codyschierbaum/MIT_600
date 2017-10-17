# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Please think of a number between 0 and 100!")
high=100
low=0
correct=1
check=""

while correct !=0:
    guess=(high+low)//2
    print ("Is your secret number ",guess ,"?")
    check = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if check == "c":
        break
    elif check =="l":
        low =guess
    elif check =="h":
        high= guess
    else: print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " , guess)