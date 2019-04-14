# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:27:49 2019

@author: abc
"""

# Python code to remove duplicate elements 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
final_list = [] 
for num in duplicate: 
	if num not in final_list: 
		final_list.append(num) 
print(final_list) 
	 
 
 
