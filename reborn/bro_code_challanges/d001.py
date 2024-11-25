# Exercise 1 Rectangle Area calc

print("Para calcular a area de um retangulo precimos que nos forneca algumas informacoes")

length = int(input("Qual a largura dele? "))
width = int(input("Qual o comprimento? "))

area = width * length
one_triangle_area = float(area / 2)

print(f"Esse retangulo teria uma area de {area} e dois triangulos de area {one_triangle_area}cm².")
