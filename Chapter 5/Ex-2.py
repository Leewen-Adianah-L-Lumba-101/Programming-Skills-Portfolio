# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:58:27 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 5: Dictionaries
"""
# Exercise 2: Glossary
# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.    

# As long as the curly brackets are present in the syntax, the data in the dictionary doesn't have to be in one long line
# It can act in the same way as """ quotations do when writing things in new lines
x = {
     "String": "A data type for a set of characters", 
     "Integer": "A data type for a whole number", 
     "Float": "A data type for a decimal" , 
     "Print": "A command that makes the output the assigned data", 
     "Input" : "A command which asks for a user to add data", 
     "Sort" : "A command to sort a list in alphabetical order"
     }

# The key is printed alongside the value of the key (which is the meaning of the programming words)
print('String' + ":", x['String'], "\n")
print('Integer' + ":", x['Integer'], "\n")
print('Float' + ":",x['Float'], "\n")
print('Print' + ":",x['Print'], "\n")
print('Input' + ":",x['Input'], "\n")
      
