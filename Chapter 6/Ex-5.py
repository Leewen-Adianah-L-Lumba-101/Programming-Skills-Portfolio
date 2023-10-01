# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:06:34 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 6: Loops
"""
# Exercise 5: No Pastrami

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["panini", "cuban", "bagel", "grilled cheese", "roast beef", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

# As long as there is pastrami in the list, the pop command will run and delete the pastrami
# When all the pastrami is deleted, the while loop will end
while "pastrami" in sandwich_orders:
    sandwich_orders.pop()

finished_sandwiches = sandwich_orders
print(finished_sandwiches)


            
