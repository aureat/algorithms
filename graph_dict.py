class Graph(object):

    def __init__(self, V):
        self.V = V
        self.graph = {}
        for i in range(V):
            self.graph.update({i+1: []})

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def num_edges_of(self, v):
        return len(self.graph[v])

    def __len__(self):
        return self.V

    def __getitem__(self, key):
        return self.graph[key]

# g = Graph(6)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(1,5)
# g.add_edge(5,6)
