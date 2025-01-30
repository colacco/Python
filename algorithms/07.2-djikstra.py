# EXERCISE 7.1 - B

# GRAPHS
grafos = {}

grafos["start"] = {}
grafos["start"]["a"] = 10

grafos["a"] = {}
grafos["a"]["b"] = 20

grafos["b"] = {}
grafos["b"]["c"] = 1
grafos["b"]["end"] = 30

grafos["c"] = {}
grafos["c"]["a"] = 1

grafos["end"] = {}

# COSTS:
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["end"] = infinity

# PARENTS:
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["end"] = None

processados = []

def custo_baixo(costs):
    nodo_barato = None
    custo_barato = infinity
    for nodo in costs:
        cost = costs[nodo]
        if cost < custo_barato and nodo not in processados:
            custo_barato = cost
            nodo_barato = nodo
    return nodo_barato

nodo = custo_baixo(costs)
while nodo is not None:
    vizinhos = grafos[nodo]
    for n in vizinhos.keys():
        novo_custo = costs[nodo] + vizinhos[n]
        if novo_custo < costs[n]:
            costs[n] = novo_custo
            parents[n] = nodo
    processados.append(nodo)
    nodo = custo_baixo(costs)

print(f"Esses são os pais {parents}")
# I make almost all code, but there's something i forgot. The "processados" didn't have append, so the code would run forever... Like the book say, how this algorithm is considered important, I'm focusing to learn very well how to code and the reasoning of it.