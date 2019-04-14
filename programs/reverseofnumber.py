# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:43:19 2019

@author: abc
"""
reverse=0
num=int(input("enter the number"))
while num>0:
    a=num%10
    reverse=(reverse*10)+a
    num=num//10
print("reverse of the number is:",reverse)    