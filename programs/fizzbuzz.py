# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:25:32 2019

@author: abc
"""

num=int(input("enter the number:"))
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ")
    elif i%3==0:
        print("RED")
    elif i%5==0:
        print("BLACK")
    else:
        print(i)    
    