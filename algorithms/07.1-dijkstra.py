# EXERCISE 7.1 - A

# GRAPHS
grafos = {}
grafos["start"] = {}
grafos["start"]["a"] = 5
grafos["start"]["b"] = 2

grafos["a"] = {}
grafos["a"]["c"] = 4
grafos["a"]["d"] = 2

grafos["b"] = {}
grafos["b"]["a"] = 8
grafos["b"]["d"] = 7

grafos["c"] = {}
grafos["c"]["d"] = 6
grafos["c"]["end"] = 3

grafos["d"] = {}
grafos["d"]["end"] = 1

grafos["end"] = {}

#COSTS:
infinito = float("inf")
custos = {}
custos["a"] = 5
custos["b"] = 2
custos["c"] = infinito
custos["d"] = infinito
custos["end"] = infinito

# PARENTS
pais = {}
pais["a"] = "start"
pais["b"] = "start"
pais["c"] = None
pais["d"] = None
pais["end"] = None

processados = []

def nodo_barato(custos):
    mais_barato = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < mais_barato and nodo not in processados:
            mais_barato = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = nodo_barato(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafos[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if novo_custo < custos[n]:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = nodo_barato(custos)

print(vizinhos)
print(pais)