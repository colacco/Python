# Consegui montar parcialmente o código. Primeiramente esqueci de adicionar o íncice na linha 9, consequentemente gerando alguns erros por esstar comparando uma lista ('lis') com número ('int'). Além disso, outra questão foi a linha 16 onde eu acabei colando em range "1, len(arr)", impedindo que o elemento que sobrasse fosse para a lista "novo_arr". 
# 19:19 - Mas porque na função busca_menor eu coloquei "range(1, len(arr))" (linha 8) e funcionou normal? Aparentemente quaando eu modifiquei apenas para "range(len(arr))" continua funcionando normalmente... Mas então, porquê o autor decidiu adicionar daquela forma? Tem algo que eu ainda preciso entender em loopings?
#19:22 - Se considerarmos que um looping começa no 0 na forma default e no 1 na anotação do autor e nada mudou, podemos admitir que seja para que a máquina faça a execução de forma mais rápida? De qualquer forma, sinto que ainda não posso responder essa pergunta, mas irei anotar em meu caderno para pensar nela. 

def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordem_selação(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr

print(ordem_selação([1, 5, 7, 8, 2, 3, 10, 504, 205, 1024]))