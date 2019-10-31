""" Graph Object in its matrix representation. """

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.graph = [[0]*V for v in range(V)]

    def add_edge(self, v, w):
        self.graph[v-1][w-1] = 1
        self.graph[w-1][v-1] = 1

    def edges_of(self, v):
        return [i+1 for i,n in enumerate(self.graph[v-1]) if n == 1]

    def num_edges_of(self, v):
        return sum(self.graph[v-1])

    def vertices(self):
        return self.V

    def edges(self):
        e = 0
        for v in range(self.V):
            e += sum(self.graph[v])
        return e/2

G = Graph(4)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)
G.add_edge(2,4)
G.add_edge(3,4)
print(G.num_edges_of(2))
