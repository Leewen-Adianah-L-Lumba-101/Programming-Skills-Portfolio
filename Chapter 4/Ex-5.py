# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:18:38 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 4: Control Flow
"""
# Exercise 5: Favorite Fruit
# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# •Make a list of your three favorite fruits and call it favorite_fruits.
# •Write five if statements. Each should check whether a certain kind of fruit is in your list. 

# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favourite_fruits = ["Strawberry", "Blueberry", "Apple"]

# The if conditions check if the string is present in any of the postitions of the list.
if "Strawberry" in favourite_fruits:
    print("You really like strawberries!")

if "Blueberry" in favourite_fruits:
    print("You really like blueberries!")
    
if "Apple" in favourite_fruits:
    print("You really like apples!")

if "Bananas" in favourite_fruits:
    print("You really like bananas!")

if "Pineapple" in favourite_fruits:
    print("You really like pineapples!")