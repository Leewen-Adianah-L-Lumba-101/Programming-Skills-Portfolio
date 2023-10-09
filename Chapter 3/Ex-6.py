# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:09:16 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 3: Data Structures 
"""
# Exercise 6: Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# •Start with your program from Exercise 3-5.
# Add a new line that prints a message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# •Print a message to each of the two people still on your list, letting them know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

dinnerparty = ["Henry VIII", "Niccolo Machiavelli", "Napoleon Bonaparte", "Joe Biden", "Thom Yorke"]

for i in dinnerparty:
    print("May I invite you,", i + "," + " on over for dinner?")

print("\nA shame.", dinnerparty[0], "couldn't make it!")

dinnerparty = ["Lady Gaga", "Niccolo Machiavelli", "Napoleon Bonaparte", "Joe Biden", "Thom Yorke"]

print("\n")
for i in dinnerparty:
    print("May I invite you,", i + "," + " on over for dinner?")

print("\nOh, it appears I can only invite two people only for dinner.")


print("\nI am very sorry", dinnerparty[0], "you cannot make it to dinner.")
# This command is used to delete the very first name on the list
dinnerparty.pop(0)

print("I am very sorry", dinnerparty[0], "you cannot make it to dinner.")
# Lady Gaga is deleted, so Niccolo Machievelli will take her place, and be deleted
dinnerparty.pop(0)

print("I am very sorry", dinnerparty[0], "you cannot make it to dinner.")
# The list gets shorter, deleting Napolean Bonaparte and that makes the list have only two people left.
dinnerparty.pop(0)

print("\n")
      
# For every member left, they are still invited
for i in dinnerparty:
    print("Fortunately, you are still invited", i + "!")

# This command gets rid of all the members in the list, so all the data so the output is nothing
dinnerparty.clear()
print("\n")
print(dinnerparty)


"""
Extra code that didn't work
j = 0
x = len(dinnerparty)
while x >= 2:
    for i in dinnerparty:
        dinnerparty.pop(j)
        print("So sorry", i,"I cannot invite you over for dinner.")
        j = j + 1
        x = x - 1
"""
