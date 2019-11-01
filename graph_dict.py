class Graph(object):

    def __init__(self, V):
        self.V = V
        self.graph = {}
        for i in range(V):
            self.graph.update({i+1: []})

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def add_edge_cost(self, v, w, cost):
        self.graph[v].append((w, cost))
        self.graph[w].append((v, cost))

    def num_edges_of(self, v):
        return len(self.graph[v])

    def __len__(self):
        return self.V

    def __getitem__(self, key):
        return self.graph[key]
