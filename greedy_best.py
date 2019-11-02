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
*** Get a path for traversal
"""
def get_path_from_trav(trav, g):
    real_path = [g]
    node = g
    while trav[node] != None:
        node = trav[node]
        real_path.append(node)
    return list(reversed(real_path))
