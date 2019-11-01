# from stack import Stack
from graph_dict import Graph

def DFS(G, s):
    trav = [s]
    S = [s]
    while S:
        flag = 0
        print(S)
        for i in G.graph[S[-1]]:
            if i not in trav:
                trav.append(i)
                S.append(i)
                flag = 1
                break
        if not flag:
            S.pop()
    return trav

g = Graph(6)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(1,5)
g.add_edge(5,6)

print(g.graph)

print(DFS(g, 1))
