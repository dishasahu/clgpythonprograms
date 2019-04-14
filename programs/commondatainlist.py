# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:37:30 2019

@author: abc
"""
def common_data(list1,list2):
    result=False
    for i in list1:
        for j in list2:
            if i==j:
                result=True
                return result
    
    
    
list1=list(input("enter the 1st list:"))
list2=list(input("enter the 2nd list:"))
print(common_data(list1,list2))