def dec_to_bin(decimal):
    binario = []

    while decimal != 0:
        unidade = decimal % 2
        binario.append(unidade)

        quociente = decimal // 2
        decimal = quociente

    binario.reverse()
    

    return print(binario)

dec_to_bin(10)