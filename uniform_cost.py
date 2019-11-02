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
*** Get a path for traversal
"""
def get_path_from_trav(trav, g):
    real_path = [g]
    node = g
    while trav[node] != None:
        node = trav[node]
        real_path.append(node)
    return list(reversed(real_path))
