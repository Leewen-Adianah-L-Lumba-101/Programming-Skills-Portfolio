# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:44:29 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 6: Loops
"""
# Exercise 1: Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

# Initializing the check as True
check = True

# As long as the check is True the program will run
while check == True:
    
    answer = str(input("Enter a topping: "))
    # However, the if test will check if the input given by the user is either a topping or "quit"
    # The answer is converted to lowercase as to have any variation of quit be the same as the condition asked
    
    if answer.lower() == "quit":
        # If the answer is infact quit, the check will be assigned False, this breaks the while loop
        # As the condition for the while loop to continue is not met anymore, check is NOT True
        check = False
        
    else:
        # If the answer is not quit, the program will continue as normal
        print("I will add", answer, "to the pizza!")
        
    



    
