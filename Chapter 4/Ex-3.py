# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:00:48 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 4: Control Flow
"""
# Exercise 3: Alien Colors #3
#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_colour = 'green'

# The alien_colour is green, therefore it passes the if test.
if alien_colour == 'green':
    print("You earned 5 points!")
    
elif alien_colour == 'yellow':
    print("You earned 10 points!")

else:
    print("You earned 15 points!")
    
    
# Elif Version
alien_colour = 'yellow'

if alien_colour == 'green':
    print("You earned 5 points!")

# The alien_colour is yellow, so it passes the elif test.
elif alien_colour == 'yellow':
    print("You earned 10 points!")

else:
    print("You earned 15 points!")

    
# Else Version
alien_colour = 'red'

if alien_colour == 'green':
    print("You earned 5 points!")
    
elif alien_colour == 'yellow':
    print("You earned 10 points!")

# The alien_colour doesn't meet any of the other tests so it passes the else test.
else:
    print("You earned 15 points!")
    