#format specifiers = {value:flags} format a value based on what FLAGS ARE INSERTED

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify 
# :+ = add "plus"
# := = place sign to lefmost position
# :  = insert a space before positive numbers   
# :, = comma separator 

x = 45789.547811987
y = "Teoria do Macaco Infinito"

print(f"{x:+,.3f}") # Análise: Esse formato só é possível ao colocar como se estivesse em uma string. Não é possível realizar essas configurações fora dessa condição.
print(f"{y:>0100}")