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

# PARENTS