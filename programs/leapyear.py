# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:07:02 2019

@author: abc
"""

year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("this is leap year!")
else:
    print("not a leap year")    