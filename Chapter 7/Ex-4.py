# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:22:34 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 7: Functions
"""
# Exercise 4: Large Shirts
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# The parameters are assigned values, they will be the default values
# Once the function is called, without any given arguments, the returned values will be the same ones in the parameters
def make_shirt(size = "large", text = "I love Python"):
    print("The size of the shirt should be", size.lower())
    print("The text on the shirt is", text)

print("\n") 

# Large shirt with the default message 
make_shirt()

print("\n")

# Medium shirt with the default message
# One default value of the parameter is replaced by the size arguement, so only size is replaced
# I'm using a keyword arguement here as to properly showcase that the 'size' variable is being changed
make_shirt(size = "medium")

print("\n")

# Any size with a different message
# Both default values of the parameter are given two arguements, so they're replaced entirely
make_shirt("extra small", "I hate Python")




    