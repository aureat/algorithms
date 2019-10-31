from doubly_linked_queue import Queue
from graph_dict import Graph

def BFS(G, s):
    Q = Queue()
    Q.put(s)
    trav = [s]
    while Q:
        v = Q.get()
        for i in G[v]:
            if i not in trav:
                trav.append(i)
                Q.put(i)
    return trav

# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(1,5)
# g.add_edge(5,6)
#
# print(g.graph)
#
# print(BFS(g, 1))
