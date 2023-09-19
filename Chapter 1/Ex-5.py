# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:46:41 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 1: Getting Started With Python
"""
# Exercise 5: Compute area of Circle
# Write a Python program which accepts the radius of a circle from the user and compute the area.

# The command accesses the math library which contains all the information for the pi data.
from math import pi

radius = int(input("Enter the radius of the circle: "))

# The arithmetic operator for a number to be squared or multiplied to a power, is **
area = pi * (radius**2)

print("The area of your circle", area)
 

