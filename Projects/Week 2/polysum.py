# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:35:30 2017

@author: a0564671
"""

def polysum(n,s):
    import math
    area=(.25*n*(s**2))/(math.tan(math.pi/n))
    perim=n*s
    return round(area+(perim**2),4)
    