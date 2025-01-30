# EXERCISE 7.1 - B

#GRAPHS
grafos = {}

grafos["start"] = {}
grafos["start"]["a"] = 2
grafos["start"]["b"] = 2

grafos["a"] = {}
grafos["a"]["c"] = 2
grafos["a"]["end"] = 2

grafos["b"] = {}
grafos["b"]["a"] = 2

grafos["c"] = {}
grafos["c"]["b"] = -1
grafos["c"]["end"] = 2

grafos["end"] = {}

#Costs
costs = {}
costs["a"] = 2
costs["b"] = 2
costs["c"] = float("inf")
costs["end"] = float("inf")

#parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None

processados = []

def next_nodo(costs):
    custo_baixo = float("inf")
    nodo_mais_baixo = None
    for nodo in costs:
        cost = costs[nodo]
        if cost < custo_baixo and nodo not in processados:
            custo_baixo = cost
            nodo_mais_baixo = nodo
    return nodo_mais_baixo

nodo = next_nodo(costs)
while nodo is not None:
    cost = costs[nodo]
    vizinhos = grafos[nodo]
    for n in vizinhos.keys():
        novo_custo = cost + vizinhos[n]
        if novo_custo < costs[n]:
            costs[n] = novo_custo
            parents[n] = nodo
    processados.append(nodo)
    nodo = next_nodo(costs)

print(f"Esses são os pais {parents}")
# Reading when the code is complete is so easy. But to start the reasoning by the zero is so difficult... May I need to make more reviews by this.