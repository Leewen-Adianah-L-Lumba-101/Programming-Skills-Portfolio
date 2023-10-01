# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:21:51 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 5: Dictionaries
"""
# Exercise 4: Rivers
# Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {"Indus" : "Tibet", "Volga" : "Russia", "Yellow" : "China"}

for i in rivers:
    print("The", i, "River runs through", rivers[i])

# To make the output cleaner
print("\n")

# For every key, it will print the river
for i in rivers:
    print(i)

print("\n")

# For every key, it will print the country when [i] is called
for i in rivers:
    print(rivers[i])