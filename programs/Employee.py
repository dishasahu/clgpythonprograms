# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:19:10 2019

@author: abc
"""

class Employee:
    def __init__(self,fname,lname,monthlysalary):
        self.fname=fname
        self.lname=lname
        self.monthlysalary=monthlysalary
        print("jhghj")
    def set_method(self):
      
        self.fname=input("enter the first name:")
        self.lname=input("enter the last name:")
        self.monthlysalary=int(input("enter the salary:"))
        if self.monthlysalary<0:
            self.monthlysalary=0
        e1.get_method()
    def get_method(self):
        print("the first name is :",self.fname)
        print("last name is :",self.lname)
        print("monthly salary is :",self.monthlysalary)
 
    
#choice=(input("enter 1 for continue"))     
e1=Employee('disha','sahu','6000')
e1.set_method() 
          
        