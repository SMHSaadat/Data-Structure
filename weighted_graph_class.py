class WGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # For undirected graph

    def print_graph(self):
        print("Adjacency matrix: ")
        for row in self.graph:
            for column in row:
                print(f"{column:^3}", end=' ')
            print()
                
g = WGraph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 4, 20)
g.add_edge(1, 2, 30)
g.add_edge(1, 3, 40)
g.add_edge(2, 3, 50)
g.add_edge(3, 4, 60)
g.print_graph()

