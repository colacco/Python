# shopping cart program

products = []
prices = []
total = 0

while True:
    product = input('What product you want to buy (q to quit)? ')
    if product.lower() == "q":
        break  
    else:
        price = float(input('What is the price? $'))
        products.append(product)
        prices.append(price)


print("----- YOUR CART -----")
for product in products:
    print(product, end=" ")

for price in prices:
    total += price

print()
print(f"Your toal is ${total}")