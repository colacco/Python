# Bro Code's concession stand program

#dictionary {key:value}

menu = {"pizza" : 3.00, "nachos" : 4.50, "popcorn" : 6.00, "fries" : 2.50, "chips" : 1.00, "pretzel" : 3.50, "soda" : 3.00, "lemonade" : 4.25}

cart = []
total = 0

# In this first time he make just 3 variables while I did 4 variables.

print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-----------------------")

# The same reasoning as me

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# Using "While True" make the code more simplified. I need to make in that way if I want to evolve.

print("-------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

# Just with 'cart' and 'food', the code run very well. My 'select', 'to_buy' and 'kart' just make me mad with a lot of desnecessary information.

print()
print(f"Total is: ${total:.2f}")