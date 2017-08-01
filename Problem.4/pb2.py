# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:05:18 2017

@author: Bany
"""

import math as mt


a=float(input("Left Interval: "))
b=float(input("Right Interval: "))
N=int(input("How many iterations? "))


def F(x):

    f = x - mt.cos(x)

    return f

l = [a+(b-a)*k/N for k in range(N)]
fl = [F(l[i]) for i in range(N)]

f2 = [i for i in range(N-1) if fl[i]*fl[i+1]<=0]


for i in range(len(f2)-1):
    if (abs(f2[i+1]-f2[i])==1):
        l[f2[i]]=l[f2[i+1]]
        f2.remove(f2[i+1])



root = [l[f2[i]] for i in range(len(f2))]
print("Root is", root)







