"""
This script calculates the price of a pizza order based on user selections.

The user chooses the pizza size (Small, Medium, or Large), whether they want pepperoni,
and if they want extra cheese. The script then calculates and displays the final bill.
"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total = 0
if size == "S":
    total += 15
    if add_pepperoni == "Y":
        total += 2
        if extra_cheese == "Y":
            total += 1
            print(f"Your final bill is: ${total}.")
            print("Thank you for ordering!") 
        else:
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!")
    else:
        if extra_cheese == "Y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
        else:
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!")
      
elif size == "M":
    total += 20
    if add_pepperoni == "Y":
      total += 3
      if extra_cheese == "Y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
    else:
      if extra_cheese == "Y":
        total += 1
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
else:
    total += 25
    if add_pepperoni == "Y":
      total += 3
      if extra_cheese == "Y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
    else:
      if extra_cheese == "Y":
        total += 1
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
