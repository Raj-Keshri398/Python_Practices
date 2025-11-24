# Making a Menu dictionary
menu = {
    'dosa': 50,
    'idli': 40,
    'vada': 60,
    'rasam': 70,
    'paneer butter masala': 200,
    'naan': 30,
    'roti': 25,
}

print("Welcome to Our Restaurant")
print("Here is the Menu")
for item, price in menu.items():
    print(f"{item} : Rs {price}")

Order_total = 0

# ---- function to place the order ----
def take_order():
    global Order_total
    item = input("\nEnter the name of item from menu : ").lower()

    if item in menu:
        Order_total += menu[item]
        print(f"Your ordered item '{item}' added successfully!")
    else:
        print(f"Ordered item '{item}' not available yet!")

# ---- Main loop ----
while True:
    take_order()
    another = input("\nDo you want to add another item? (Yes/No): ").lower()

    if another != "yes":
        break

print("\n---------------------------------")
print(f"Your Final Total Bill = Rs {Order_total}")
print("Thank you for ordering!")
