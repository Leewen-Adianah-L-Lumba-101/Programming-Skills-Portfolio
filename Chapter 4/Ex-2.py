# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:55:18 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 4: Control Flow
"""
# Exercise 2: Alien Colors #2
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# •If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# •If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# •Write one version of this program that runs the if block and another that runs the else block.

alien_colour = 'green'

# The alien_colour is green, therefore it passes the if test.
if alien_colour == 'green':
    print("You just earned 5 points!")
    
else:
    print("You just earned 10 points!")
    
    
# Else Version
alien_colour = 'yellow'

if alien_colour == 'green':
    print("You just earned 5 points!")

# The alien_colour is something other than green, so it fails the if test and passes the else.
else:
    print("You just earned 10 points!")
    
    