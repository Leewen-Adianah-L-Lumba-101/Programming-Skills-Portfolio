# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:41:20 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 5: Dictionaries
"""
# Exercise 5: Pets
# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet

# This acts as the reference variable incase any animal species starts with a vowel
# So when printing statements, the if test can check this and print a more grammatically correct message
vowel = 'aeiou'

pets = [{"Iguana" : "Martin"}, {"Dog" : "Andrew"}, {"Tarantula" : "Amy"}, {"Anaconda" : "Sally"}, {"Goldfish" : "Alex"}]

# For every dictionary set in the list
for i in pets:
    # For every key and value in the dictionary set
    for j in i:
        # An extra command
        if j[0].lower() in vowel:
            print("An", j.lower(),"is owned by", i[j])
        else:
            print("A", j.lower(), "is owned by", i[j])
         
  
