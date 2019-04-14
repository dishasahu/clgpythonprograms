# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:19:33 2019

@author: abc
"""

month_num=int(input("enter the month number:"))
if month_num==2: 
    print("there are 28 days")
elif month_num==4 or month_num==6 or month_num==9 or month_num==11:
    print("there are 30 days ")
else:
    print("there are 31 days")    