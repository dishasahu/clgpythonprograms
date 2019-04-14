# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:12:23 2019

@author: abc
"""

num=int(input("enter the number:"))
if num>2:
    for i in range(2,num):
        if (num%i)==0:
            print("number is not prime")
            break
        else:
            print("number is  prime")
            break
elif num==2:
    print("number is prime")
else:
   print("number is not prime")        
        