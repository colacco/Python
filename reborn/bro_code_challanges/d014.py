# Concession stand program

eletronics = {"echo dot" : 429.00, "kindle" : 539.10, "smart tv" : 2279.05, "printer" : 1322.10, "cpu" : 839.90}
kart = []
total = 0

print("------- MENU ----------")
for key, value in eletronics.items():
    print(f"{key:10}: R$ {value}")
print("-----------------------")

select = input("Select an item (q to quit): ")

while not select == "q":
    kart.append(eletronics.get(select))
    
    select = input("Select an item (q to quit): ")

for item in kart:
    if item == None:
        continue
    else:
        total += item
    
print ("----------YOUR CART----------")
for eletronic in eletronics.values