# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:45:35 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 4: Control Flow
"""
# Exercise 1: Alien Colors #1
# Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# •Write an if statement to test whether the alien’s color is green. 
# If it is, print a message that the player just earned 5 points.

# •Write one version of this program that passes the if test and another that fails. 
# (The version that fails will have no output.)

alien_colour = 'green'

# The if condition is met therefore the output is as follows.
if alien_colour == 'green':
    print("You just earned 5 points!")


# Fail Version
alien_colour = 'red'

# The alien_colour is not green, therefore it doesn't pass the if test and there is no output.
if alien_colour == 'green':
    print("You just earned 5 points!")
