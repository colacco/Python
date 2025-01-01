# Esse capítulo não possui um algoritmo específico, porém ele da todo um contexto conceitual de como a máquina funciona por trás... Extremamente essencial para que eu consiga entender e aproveitar até os limites da capacidade de processamento e memória das máquinas. Extremamente fascinante como uma simples função criada por nós é uma complexidade por trás.

def fat(x):
    if x == 1:
        return 1 # Caso base, condição necessária para que o código pare de ser executado e não siga infinitamente
    else:
       return x * fat(x-1) # recursão: retoma à própria função

print(fat(7))