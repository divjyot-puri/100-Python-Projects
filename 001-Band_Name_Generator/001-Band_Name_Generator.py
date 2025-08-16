"""
This script generates a band name by combining the user's city and pet names.

The program prompts the user for their city and pet names and then displays a suggested band name.
"""

print("Welcome to the Band Name Generator")
print("What's the name of the city you grew up in?")
city = input("Enter city's name: ")
print("What's the name of your pet?")
pet = input("Enter pet's name: ")
print(f"The name of the band could be: {city} {pet}")
