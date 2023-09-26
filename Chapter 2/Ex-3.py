# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:56:23 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 2- Variables & Comments
"""
# Exercise 3: Stripping Names 
# Tidy up the code to make it easier to understand
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


name = "\tAdam\t"
print(name)

# The space in this case is the command \t
# The command .lstrip, removes the space from the left side of the 'name' variable.
print("\n", name.lstrip())

# The command .rstrip, removes the space from the right side of the 'name' variable.
print("\n", name.rstrip())

# The command .strip, removes the space from both left and right side of the 'name' variable.
print("\n", name.strip())