# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:45:35 2019

@author: abc
"""

class student:
    def __init__(self):
        print("constructor is being called!!")
    def __del__(self):
        print("destructor is being called!!")
        
s1=student()
del s1        