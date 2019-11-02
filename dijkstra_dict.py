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
