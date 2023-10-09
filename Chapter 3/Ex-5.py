# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:20:23 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 3: Data Structures 
"""
# Exercise 5: Change Guest List
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# •Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can’t make it.
# •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# •Print a second set of invitation messages, one for each person who is still in your list

dinnerparty = ["Henry VIII", "Niccolo Machiavelli", "Napoleon Bonaparte", "Joe Biden", "Thom Yorke"]

for i in dinnerparty:
    print("May I invite you,", i + "," + " on over for dinner?")

# The first name on the list, which is Henry VIII could not make it
print("A shame.", dinnerparty[0], "couldn't make it!")

# Replacing Henry VIII with Lady Gaga, modifying the list
dinnerparty = ["Lady Gaga", "Niccolo Machiavelli", "Napoleon Bonaparte", "Joe Biden", "Thom Yorke"]

# Using for loop to go through everything again on the modified list and printing a message for each name
for i in dinnerparty:
    print("May I invite you,", i + "," + " on over for dinner?")


