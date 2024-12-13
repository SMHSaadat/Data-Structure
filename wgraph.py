class Node:
    def __init__(self, vertex):
        self.vertex = vertex  # Destination vertex of the edge
        self.next = None  # Pointer to the next node

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex  # The vertex id
        self.adj_list = None  # Circular linked list of outgoing edges

class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex(i) for i in range(num_vertices)]  # Create vertices

    def add_edge(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            new_node = Node(to_vertex)

            # Get the adjacency list of the from_vertex
            from_vertex_node = self.vertices[from_vertex]

            # If adjacency list is empty, set the node to point to itself (circular)
            if not from_vertex_node.adj_list:
                from_vertex_node.adj_list = new_node
                new_node.next = new_node  # Circular link to itself
            else:
                # Otherwise, add the new node to the circular linked list
                current = from_vertex_node.adj_list
                while current.next != from_vertex_node.adj_list:
                    current = current.next
                current.next = new_node
                new_node.next = from_vertex_node.adj_list

        else:
            print("Vertex index out of bounds.")

    def remove_edge(self, from_vertex, to_vertex):
        """Remove the directed edge from `from_vertex` to `to_vertex`."""
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            from_vertex_node = self.vertices[from_vertex]

            if not from_vertex_node.adj_list:
                print(f"No edges from vertex {from_vertex}.")
                return

            current = from_vertex_node.adj_list
            previous = None

            while True:
                if current.vertex == to_vertex:
                    if previous:
                        previous.next = current.next
                    else:
                        # Special case: removing the first node
                        if current.next == from_vertex_node.adj_list:
                            from_vertex_node.adj_list = None  # No more edges
                        else:
                            # Find the last node to update the circular link
                            temp = from_vertex_node.adj_list
                            while temp.next != from_vertex_node.adj_list:
                                temp = temp.next
                            temp.next = current.next
                            from_vertex_node.adj_list = current.next
                    print(f"Edge from {from_vertex} to {to_vertex} removed.")
                    return
                previous = current
                current = current.next
                if current == from_vertex_node.adj_list:
                    break

            print(f"Edge from {from_vertex} to {to_vertex} not found.")
        else:
            print("Vertex index out of bounds.")

    def display_graph(self):
        for vertex in self.vertices:
            print(f"Vertex {vertex.vertex}:", end=" ")
            if vertex.adj_list:
                current = vertex.adj_list
                while True:
                    print(f"{current.vertex}", end=" -> ")
                    current = current.next
                    if current == vertex.adj_list:
                        break
                print("Back to start")
            else:
                print("No edges.")


graph = DirectedGraph(4)

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)

graph.display_graph()
