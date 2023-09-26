# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:07:49 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 3: Data Structures 
"""
# Exercise 4: Guest List 
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

dinnerparty = ["Henry VIII", "Niccolo Machiavelli", "Napoleon Bonaparte", "Joe Biden", "Thom Yorke"]

# Using a for loop again to invite each person on the list with their name
for i in dinnerparty:
    print("May I invite you,", i + "," + " on over for dinner?")