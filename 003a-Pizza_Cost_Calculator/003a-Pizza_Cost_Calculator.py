"""
This script calculates the price of a pizza order based on user selections.

The user chooses the pizza size (Small, Medium, or Large), whether they want pepperoni,
and if they want extra cheese. The script then calculates and displays the final bill.
"""
simple_banner = """
    ╔═══════════════════════════════════════╗
    ║           🍕 PIZZA DELIVERY 🍕        ║
    ║                                       ║
    ║     ____  _                           ║
    ║    |  _ \\(_)__________ _              ║
    ║    | |_) | |_  /_  / _` |             ║
    ║    |  __/| |/ / / / (_| |             ║
    ║    |_|   |_/___/___\\__,_|             ║
    ║                                       ║
    ║         🛵 Fast Delivery! 🛵          ║
    ║      "Hot pizza, delivered fast!"     ║
    ╚═══════════════════════════════════════╝
    """
print(simple_banner)
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
total = 0
if size == "s":
    total += 15
    if add_pepperoni == "y":
        total += 2
        if extra_cheese == "y":
            total += 1
            print(f"Your final bill is: ${total}.")
            print("Thank you for ordering!") 
        else:
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!")
    else:
        if extra_cheese == "y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
        else:
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!")
      
elif size == "m":
    total += 20
    if add_pepperoni == "y":
      total += 3
      if extra_cheese == "y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
    else:
      if extra_cheese == "y":
        total += 1
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
else:
    total += 25
    if add_pepperoni == "y":
      total += 3
      if extra_cheese == "y":
          total += 1
          print(f"Your final bill is: ${total}.")
          print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
    else:
      if extra_cheese == "y":
        total += 1
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!") 
      else:
        print(f"Your final bill is: ${total}.")
        print("Thank you for ordering!")
