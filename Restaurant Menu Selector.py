print("\nToday's Menu")
print("1. Pizza - 100/-")
print("2. Burger - 50/-")
print("3. Ice-cream - 70/-")
choice = int(input("Enter the Menu Number: "))
quantity = int(input("Enter the Quantity: "))
item = ""
price = 0
if choice == 1:
    item = "Pizza"
    price = 100
elif choice == 2:
    item = "Burger"
    price = 50
elif choice == 3:
    item = "Ice-cream"
    price = 70
else:
    item ="Invalid Choice"
total_price = price*quantity
if item != "Invalid Choice":
    print("item: ", item)
    print(f"price: {price}/-")
    print(f"total_price: {total_price}/-")
else:
    print("Invalid Choice! please select correct menu number")