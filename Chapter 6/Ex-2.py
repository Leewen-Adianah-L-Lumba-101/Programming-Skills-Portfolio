# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:36:45 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 6: Loops
"""
# Exercise 2: Movie Tickets
# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
       
check = True

while check == True:
    
    # A simple reminder to the prices of the tickets
    print("")
    print("\t\t  TICKET PRICES:\t\t")
    print("====================================")
    print("Under 3: FREE!\nBetween 3 and 12: $10\nOver 12: $15")
    print("====================================")
    answer = float(input("How many tickets do you wish to buy? "))
    
    # If no tickets are wished to be bought, the program will stop entirely, while loop ends
    if answer == 0:
       check = False
       print("No tickets bought.")
    
    # I made the prorgam as to accomodate buying multiple tickets in one go
    else:
        # Initializing the total for all tickets as well as converting total back to float
        total = 0
        check2 = answer
        
        # The 'answer' variable will remain untouched as for the if test in the end to work correctly
        # As long as the 'check 2' has the same data as 'answer' it will continue adding the ticket totals
        # Every age will be checked and given the price then added to the total until the 'check2' is decremented to 0
        while check2 > 0:
            age = int(input("Enter the age: "))
            
            if age < 3:
                ticket = 0
            elif age >= 3 and age <=12:
                ticket = 10
            else:
                ticket = 15
            
            # Once the ticket price is decided by the if conditions, it will add it to the total
            total = total + ticket
            check2 -= 1
            # Once the check2 is decremented, the while loop can start checking again for the other age

        # After the check2 is completely 0, there is no one left to give tickets to
        # The program proceeds to checkout and tell the user how much they need to pay
        # The total will be converted to string, as to add the dollar sign symbol correctly
        # If it weren't string, it would send the message out with a space inbetween the two
        
        total = str(total)
        
        # For grammar's sake, if only one ticket was bought, the message would be as following
        # Here we needed the 'answer' variable intact so I used 'check2'
        if answer == 1:
            print("The total for the ticket is $" + total)
        else:
            print("Your total for the tickets are $" + total)           
        
        
        