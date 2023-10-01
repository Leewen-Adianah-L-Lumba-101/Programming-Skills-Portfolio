# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:40:37 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 6: Loops
"""
# Exercise 4: Deli
# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.


sandwich_orders = ["panini", "cuban", "bagel", "grilled cheese", "roast beef"]
finished_sandwiches = []

# For every sandwich that's made, it will be added to the empty 'finished_sandwiches' list
for i in sandwich_orders:
    print("I made your", i,"sandwich.")
    finished_sandwiches.append(i)

print("\n")

print("All the sandwiches that have been made are: ")

# For every sandwich in the newly added finished_sandwiches list, it's printed out indivudually
for i in finished_sandwiches:
    print(i)
