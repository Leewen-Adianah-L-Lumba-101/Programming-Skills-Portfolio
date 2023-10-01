# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:09:04 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 7: Functions
"""
# Exercise 3: T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print("The size of the shirt should be", size.lower())
    print("The text on the shirt is '" + text + "'")

# Positional arguements are used when relying on the position of the function's parameters to assign the values
make_shirt("small", "Swagger")

# Keyword arguements are more specific, it's explicity calling the function's parameters and assigning them values
# So even if the position of the text is on the parameter position 'size', it will only be assigned to 'text'
make_shirt(text = "Filipino", size = "large")