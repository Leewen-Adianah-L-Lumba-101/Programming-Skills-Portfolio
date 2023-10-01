# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:22:29 2023

@author: Leewen Adianah L. Lumba
"""

"""
Chapter 7: Functions
"""
# Exercise 5: Cities
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country = "Germany"):
    # Uppercase for the first letter in the city and country
    print("The city", city.capitalize(), "is in", country.capitalize())
    
# Default country, there's no other arguement given alongside Berlin so Germany is still the default second parameter
describe_city("Berlin")

print("\n")

# Second city
# The introduction of the "China" data will now overwrite the "Germany" data
# There's no default value in city, so I'll be using a positional arguement
# There's no difference in using a keyword or positional here
# I only want to use it to show which arguement goes against which parameter in clarity
describe_city("beijing", country = "China")

print("\n")

# Third city
describe_city("amsterdam", country = "netherlands")


   