class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.adj_matrix[i][i] = 0  # Distance to itself is zero

    def add_edge(self, u, v, weight):

        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph
        else:
            raise ValueError("Vertex index out of bounds")

    def display(self):

        for row in self.adj_matrix:
            print(" ".join(map(lambda x: str(x) if x != float('inf') else 'inf', row)))

g = WeightedGraph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 4, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 4, 3)
g.add_edge(3, 4, 6)
g.add_edge(4, 5, 1)
g.display()
