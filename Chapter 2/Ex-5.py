# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:14:24 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 2- Variables & Comments
"""
# Exercise 5: USB Shopper
# A girl heads to a computer shop to buy some USB sticks.
# She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.


# This arithmetic operator divides 50 by 6 but only leaves the integer remainder as the answer.
# It divides 50 by 6 because each stick is £6 and she only has £50, therefore for every £6 in £50:
# It's equivalent to ONE USB stick. However, £50 is not divisible by £6 so the number of USB sticks that
# can be bought are 8, and she will have a leftover of £2 pounds as she cannot afford another USB stick.
USBsticks = 50//6

# The integer remainder for USBsticks is then multiplied by 6, which is the price for each USB stick.
price = USBsticks * 6

print("She can buy around", USBsticks, "USB sticks. For the price of £", price)
