# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:30:31 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 3: Data Structures 
"""
# Exercise 7: Seeing the World
# Think of at least five places in the world you’d like to visit. 
# • Store the locations in a list. 
# Make sure the list is not in alphabetical order.

# • Print your list in its original order. 
# Don’t worry about printing the list neatly, just print it as a raw Python list.

# • Use sorted() to print your list in alphabetical order without modifying the actual list.

# • Show that your list is still in its original order by printing it.

# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

# • Show that your list is still in its original order by printing it again.

# • Use reverse() to change the order of your list. 
# Print the list to show that its order has changed.

# • Use reverse() to change the order of your list again. 
# Print the list to show it’s back to its original order.

# • Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.


visit = ["Venice", "Hokkaido", "Berlin", "Alberta", "Rome", "Madagascar"]
print(visit)

# Sorts the list 'visit' in alpgabetical order
visit.sort()
print("\n",visit)

# Returning the list to the original state by reinitializing the list with the original data
visit = ["Venice", "Hokkaido", "Berlin", "Alberta", "Rome", "Madagascar"]
# I printed the list in the next line to make the printing statements less cluttered when the program is run
print("\n",visit)

# Sorts the list again in reverse alphabetical order
visit.sort(reverse = True)
print("\n",visit)

# Returning the list to the original state by reinitializing the list with the original data
visit = ["Venice", "Hokkaido", "Berlin", "Alberta", "Rome", "Madagascar"]
print("\n",visit)

# Puts the list in descending order from the last place as the first, second last as the second and so on...
visit.reverse()
print("\n",visit)

# Puts the reversed list in reverse, making it return to the original order once more
visit.reverse()
print("\n",visit)

visit.sort()
print("\n",visit)

visit.sort(reverse = True)
print("\n",visit)
