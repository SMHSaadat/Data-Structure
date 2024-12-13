class WDGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, s, t, weight):
        if 0 <= s < self.vertices and 0 <= t < self.vertices:
            self.adjacency_matrix[s][t] = weight
        else:
            print("Vertex index out of bounds.")
            return None

    def remove_edge(self, s, t):
        if 0 <= s < self.vertices and 0 <= t < self.vertices:
            self.adjacency_matrix[s][t] = 0
        else:
            print("Vertex index out of bounds.")
            return None

    def get_weight(self, s, t):
        if 0 <= s < self.vertices and 0 <= t < self.vertices:
            return self.adjacency_matrix[s][t]
        else:
            print("Vertex index out of bounds.")
            return None

    def display_graph(self):
        print("Adjacency matrix: ")
        for row in self.adjacency_matrix:
            for column in row:
                print(f"{column:^3}", end=' ')
            print()

graph = WDGraph(4)

graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 0, 40)

graph.display_graph()


