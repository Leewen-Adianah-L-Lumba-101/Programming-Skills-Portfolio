# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:59:05 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 7: Functions
"""
# Exercise 2: Favourite Book
# Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is Alice in Wonderland. 
# Call the function, making sure to include a book title as an argument in the function call.

# The parameter acts as a placeholder variable
def favourite_book(title):
    print("One of my favourite books is", title)

# When the function is called, anything inside the bracket is considered a valid arguement
# It will add value to the placeholder variable (aka parameter) 'title'
favourite_book("1984")