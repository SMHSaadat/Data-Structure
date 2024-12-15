class DGraph:
    def __init__(self, vertices):

        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):

        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
        else:
            raise ValueError("Vertex index out of bounds")

    def remove_edge(self, u, v):

        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 0
        else:
            raise ValueError("Vertex index out of bounds")

    def bfs(self, start):

        if not (0 <= start < self.vertices):
            raise ValueError("Start vertex index out of bounds")

        visited = [False] * self.vertices
        queue = [start]
        bfs_order = []

        visited[start] = True

        while queue:
            current = queue.pop(0)
            bfs_order.append(current)

            for neighbor in range(self.vertices):
                if self.adj_matrix[current][neighbor] != 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return bfs_order

    def dfs(self, start):

        if not (0 <= start < self.vertices):
            raise ValueError("Start vertex index out of bounds")

        visited = [False] * self.vertices
        stack = [start]
        dfs_order = []

        while stack:
            current = stack.pop()

            if not visited[current]:
                visited[current] = True
                dfs_order.append(current)

                # Push neighbors to the stack in reverse order to maintain order
                for neighbor in range(self.vertices - 1, -1, -1):
                    if self.adj_matrix[current][neighbor] != 0 and not visited[neighbor]:
                        stack.append(neighbor)

        return dfs_order

    def display(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.display()

print("BFS starting from vertex 0:", g.bfs(0))
print("DFS starting from vertex 0:", g.dfs(0))
