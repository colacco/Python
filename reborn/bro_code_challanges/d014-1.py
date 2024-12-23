# Concession stand program

eletronics = {"echo dot" : 429.00, "kindle" : 539.10, "smart tv" : 2279.05, "printer" : 1322.10, "cpu" : 839.90}
kart = []
to_buy = []
total = 0

print("------- MENU ----------")
for key, value in eletronics.items():
    print(f"{key:10}: R$ {value:.2f}")
print("-----------------------")

select = input("Select an item (q to quit): ").lower()

while not select == "q":
    kart.append(eletronics.get(select))
    if eletronics.get(select) is not None:
        to_buy.append(select)

    select = input("Select an item (q to quit): ").lower()

for item in kart:
    if item == None:
        continue
    else:
        total += item
    
print ("----------YOUR CART----------")
for buy in to_buy:
    print(buy, end=" ")

print()
print(f"The total is R$ {total:.2f}")

# Analysis: My code is so confusing, the name of variables can't help with that. I make 3 loops in  this code  while Bro Code made just 1. But for my first program I am really happy with the result, is not what i wanted, but i like. The most important now is:
# - Focus in better names for variables
# - Try to reduces rows of code