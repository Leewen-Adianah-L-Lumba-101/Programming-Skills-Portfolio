# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:07:02 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 5: Dictionaries
"""
# Exercise 3: Glossary 2
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

# Five new words with their meanings are added on to the list
x = {
     "String": "A data type for a set of characters", 
     "Integer": "A data type for a whole number", 
     "Float": "A data type for a decimal" , 
     "Print": "A command that makes the output the assigned data", 
     "Input" : "A command which asks for a user to add data", 
     "Sort" : "A command to sort a list in alphabetical order",
     "Pop": "A command to remove something from a list",
     "Compiler" : "A translator that runs the source code to bytecode",
     "Interpreter" : "A translator that runs source code to bytecode line by line when executed",
     "Increment" : "Increase the value/number of something, which is usually done in a while loop"
     }

# For each key in the dictionary, it will be printed along with the respective value
# Instead of having to print every key alongside the value continously, we can use a for loop

for i in x:
    print(i + ":", x[i], "\n")
    