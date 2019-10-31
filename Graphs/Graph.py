class Graph(object):

    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    def add_edge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def get_graph(self):
        print(self.graph)


g = Graph(4)
g.add_edge(0,1)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(1,2)
g.get_graph()
