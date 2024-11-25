# shopping

item = input("O que voce quer comprar? ")
preco = float(input("Qual é o valor(R$)? "))
quantity = float(input("Quantos voce ira comprar? "))

price = preco / 5.8 #in november 2024
btc = preco / 561358.45 
eur = preco / 6.06
total_preco = str(quantity * preco)
total_price = str(quantity * price)
total_btc = str(quantity * btc)
total_eur =  str(quantity * eur)

print(f"Em novembro voce gastaria R${total_preco} que é igual a:")
print(f"U${total_price} em dolar")
print(f"{total_btc} em BTC")
print(f"${total_eur} em euro")