from priority_queue import PriorityQueue
from graph_dict import Graph

"""
***   Greedy Best-First Search
***   arg G: Dictionary graph object
***   arg s: Starting node label
***   arg g: Goal node label
***
***   returns an ordered list of nodes as shortest path to the goal
"""
def greedy_best(G, s, g):
    Q = PriorityQueue()
    Q.put(s, heuristic(s))
    trav = {s: None}
    while Q:
        v = Q.getMin()
        if v == g:
            break
        for j in G[v]:
            if j[0] not in trav:
                priority = heuristic(j[0])
                Q.put(j[0], priority)
                trav[j[0]] = v
    # print(total_cost)
    return get_path_from_trav(trav, g)


"""
***   Uniform Cost Search (also: search version of Dijkstra's Algorithm)
***   arg G: Dictionary graph object
***   arg s: Starting node label
***   arg g: Goal node label
***
***   returns an ordered list of nodes as shortest path to the goal
"""
def uniform_cost(G, s, g):
    Q = PriorityQueue()
    Q.put(s, 0)
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
                priority = cost
                Q.put(j[0], priority)
                trav[j[0]] = v
    # print(total_cost)
    return get_path_from_trav(trav, g)

"""
***   Dijkstra's Algorithm
***   arg G: Dictionary graph object
***   arg s: Starting node label
***   arg l: A starting node to traverse from
***
***   return total_cost: Dictionary of shortest distances to each node in a graph
"""
def dijkstra(G, s, l):
    Q = PriorityQueue()
    Q.put(s, 0)
    trav = {s: None}
    total_cost = {s: 0}
    while Q:
        v = Q.getMin()
        for j in G[v]:
            cost = total_cost[v] + j[1]
            if j[0] not in trav or cost < total_cost[j[0]]:
                total_cost[j[0]] = cost
                priority = cost
                Q.put(j[0], priority)
                trav[j[0]] = v
    # print(total_cost)
    return total_cost

"""
***   A-Star Search
***   arg G: Dictionary graph object
***   arg s: Starting node label
***   arg g: Goal node label
***
***   returns an ordered list of nodes as shortest path to the goal
"""
def a_star(G, s, g):
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
    # print(total_cost)
    return get_path_from_trav(trav, g)

"""
***   Heuristics Method
"""
def heuristic(node):
    return hs.get(node)

"""
*** Get a path for traversal
"""
def get_path_from_trav(trav, g):
    real_path = [g]
    node = g
    while trav[node] != None:
        node = trav[node]
        real_path.append(node)
    return list(reversed(real_path))

"""
***   Problem statement.
***   Given a graph with heuristics pre-given find the optimal path to the goal state G
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

print(dijkstra(G, 1, 5))
