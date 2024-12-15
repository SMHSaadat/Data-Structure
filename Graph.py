class Cqueue:
    def __init__(self, limit=10) -> None:
        self.Q = [None] * limit
        self.limit = limit
        self.rear = -1
        self.front = -1

    def insert_queue(self, data):
        if (self.rear+1) % self.limit == self.front:
            print('full')
            return -1

        elif self.front == -1:
            self.front += 1
            self.rear += 1
            self.Q[0] = data

        else:
            self.rear  = (self.rear+1) % self.limit
            self.Q[self.rear] = data

    def delete_queue(self):
        if self.front == -1:
            # print("empty")
            return None

        elif self.front == self.rear:
            a = self.front
            self.front= -1
            self.rear = -1
            return self.Q[a]

        else:
            b = self.front
            self.front = (self.front+1) % self.limit
            return self.Q[b]

    def display(self):
        if self.rear == -1 and self.front == -1:
            print("empty")
            return -1
        elif self.front <= self.rear:
            for i in range(self.front, self.rear+1):
                print(self.Q[i])
        else:
            for i in range(self.front, self.limit):
                print(self.Q[i])

            for i in range(0, self.rear + 1):
                print(self.Q[i])
                
    def replace(self, data, new_data):
        flag = False
        if self.rear == -1 and self.front == -1:
            print("empty")
        else:
            if self.front< self.rear:
                for i in range(self.front, self.rear + 1):
                    if self.Q[i] == data:
                        self.Q[i] =  new_data
                        flag = True
            elif self.front == self.rear:
                if self.Q[self.front] == data:
                    self.Q[self.front] = new_data
                    flag = True
            elif self.front > self.rear:
                for i in range(self.front, self.limit):
                    if self.Q[i] == data:
                        self.Q[i] = new_data
                        flag = True
                for i in range(0, self.rear+1):
                    if self.Q[i] == data:
                        self.Q[i] =  new_data
                        flag = True
        if not(flag):
            print("Your data not found")
                
class Stack:
    def __init__(self, limit=100):
        self.stack = []
        self.limit = limit

    def peek(self):
        if len(self.stack) != 0:
            return -1
        else:
            return self.stack[-1]

    def push(self, data):
        if len(self.stack) > self.limit:
            return -1
        else:
            self.stack.append(data)

    def pop(self):

        if len(self.stack) >= 0:
            return self.stack.pop()
        else:
            return -1

    def find(self, data):
        if len(self.stack) <= 0:
            return -1
        for i in range(1, len(self.stack)):
            if self.stack[i] == data:
                return i
        return -1
    def replace(self, data, new_data):
        if len(self.stack) <= 0:
            return -1
        else:
            if data in self.stack:
                self.stack[self.stack.index(data)] = new_data
            else:
                return -1

    def show(self):
        for i in self.stack:
            print(i)

    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:
            print("Vertex index out of bounds")
            return None

    def bfs(self, start):
        if (0 <= start < self.vertices):

            visited = [False] * self.vertices
            queue = Cqueue()
            queue.insert_queue(start)
            bfs_order = []

            visited[start] = True

            while queue.front!=-1:
                current = queue.delete_queue()
                bfs_order.append(current)

                for neighbor in range(self.vertices):
                    if self.adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.insert_queue(neighbor)
            print(f"BFS starting from vertex {start}: ", end='')
            return bfs_order

    def dfs(self, start):
        if (0 <= start < self.vertices):
            visited = [False] * self.vertices
            stack = Stack()
            stack.push(start)
            dfs_order = []

            while not (stack.is_empty()):
                current = stack.pop()

                if not visited[current]:
                    visited[current] = True
                    dfs_order.append(current)

                    # Push neighbors to the stack in reverse order to maintain order
                    for neighbor in range(self.vertices - 1, -1, -1):
                        if self.adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                            stack.push(neighbor)
            print(f"DFS starting from vertex {start}: ", end='')
            return dfs_order

    def display(self):
        print("Adjacency matrix: ")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 0)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(4, 3)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(5, 4)
g.display()


print(g.bfs(1))
print(g.dfs(1))
