#HASH OF GRAPH
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

#HASH OF COSTS
infinity = float("inf") # DEFINITION OF INFINITY IN PYTHON
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#HASH OF PARENTS:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None 

procesed = []


def find_lowest_cost(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in procesed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost(costs)
while node is not None:
    cost = costs[node] #SET THE COST TO GO 
    neighbors = graph[node] # SET *ALL* NEIGHBORS OF THE REFERENCE NODE
    for neighbor in neighbors.keys(): # FOR UPDATE A NEW COST IF HAS A LOWER COST THAN THE ONE ANALYSED
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost: #COMPARE
            costs[neighbor] = new_cost # UPDATE A NEW COST
            parents[neighbor] = node # UPDATE A PARENT 
    procesed.append(node) # -1 NODE
    node = find_lowest_cost(costs)

print(parents)
print(costs)