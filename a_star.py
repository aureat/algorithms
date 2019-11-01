from priority_queue import PriorityQueue
from graph_dict import Graph

"""
***   arg G: Dictionary graph object
***   arg s: Starting node label
***   arg g: Goal node label
***   arg hs: Heuristic table lookup per label in G (optional)
***
***   return trav: Dictionary of from which we node come to a current node
"""
def a_star(G, s, g, hs):
    Q = PriorityQueue()
    Q.put(s, heuristic(s))
    trav = {s: None}
    total_cost = {s: 0}
    while Q:
        v = Q.getMin()
        if v == g:
            break
        for j in G[v]:
            cost = total_cost[v] + j[1]
            if j[0] not in trav or cost < total_cost[j[0]]:
                total_cost[j[0]] = cost
                priority = cost + heuristic(j[0])
                Q.put(j[0], priority)
                trav[j[0]] = v
    return trav

"""
***   Heuristics Method
"""
def heuristic(node):
    return hs.get(node)

"""
***   Problem statement.
***   Given a graph with heuristics pre-give find the optimal path to the goal state G
"""
G = Graph(5)
G.add_edge_cost(1,2,1)
G.add_edge_cost(1,3,4)
G.add_edge_cost(2,3,2)
G.add_edge_cost(2,4,5)
G.add_edge_cost(2,5,12)
G.add_edge_cost(3,4,2)
G.add_edge_cost(4,5,3)

hs = {1: 7, 2: 6, 3: 2, 4: 1, 5: 0}

print(a_star(G, 1, 5, hs))
