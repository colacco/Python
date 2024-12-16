
# Requerimento de alteração de endereço de CNH de 2024. Não é um programa para ser usado, é apenas um treinamento pessoal para a melhor compreessão de funções.
def req_alt_end():
    print(f"Eu,{nome}")
    print(f"Nome social (opcional) - Decreto 55.588/2010, {nome_social}")
    print(f"portador do RG {rg}, CPF {cpf},")
    print("venho por meio deste comunicar a alteração de meu endereço para,")
    print(f"{rua}")
    print(f"nº {num}, complemento {comp}, bairro {bairro}")
    print(f"cidade {cidade}, estado {estado}, CEP {cep}")
    print(f"Declaro que estas informações constituem a expressão da verdade, sujeitando-me às penas da lei na hipótese de falsidade. ")
    print(f"{cid_atual}, {dia} de {mes} de {ano}")
    input("As informações acima estão corretas (s/n)?: ")

print("Sua CNH precisa ser alterada de endereço para fazermos a renovação. Farei algumas perguntas para você.")

nome = input("Qual seu nome?: ")
nome_social = None
rg = input("Qual seu RG?: ")
cpf = input("Qual seu CPF?: ")
rua = input("Qual a rua você mora?: ")
num = input("Qual o número da residência?: ")
comp = None
bairro = input("Qual é o bairro?: ")
cidade = input("Qual a cidade do endereço?: ")
estado = input("Qual o estado?: ")
cep = input("Qual o CEP?: ")
cid_atual = input("Qual cidade você está respondendo esse questionário?:")
dia = input("Qual o dia de hoje?: ")
mes = input("E o mês?: ")
ano = input("E o ano?: ")

req_alt_end()