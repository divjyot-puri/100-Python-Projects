"""
This script calculates how much each person should pay for a bill, including a tip.

It prompts the user for the total bill, the desired tip percentage, and the number of people splitting the bill.
It then calculates and displays the amount each person should pay.
"""
print("Welcome to the Tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15: "))
person = int(input("How many people to split the bill: "))
total = round(((bill + (tip/100)*bill)/person), 2)
print(f"Each person should pay: {total}")
