class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex  # Destination vertex
        self.weight = weight  # Edge weight
        self.next = None  

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex  # The vertex id
        self.adj_list = None  # Circular linked list of edges

class WeightedDirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex(i) for i in range(num_vertices)]

    def add_edge(self, from_vertex, to_vertex, weight):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            new_node = Node(to_vertex, weight)
            
            # Add the new node to the adjacency list of the from_vertex
            from_vertex_node = self.vertices[from_vertex]
            
            # If adjacency list is empty, set the node to point to itself (circular)
            if not from_vertex_node.adj_list:
                from_vertex_node.adj_list = new_node
                new_node.next = new_node  # Circular link to itself
            else:
                # Otherwise, add the node to the circular list at the end
                current = from_vertex_node.adj_list
                while current.next != from_vertex_node.adj_list:
                    current = current.next
                current.next = new_node
                new_node.next = from_vertex_node.adj_list

        else:
            print("Vertex index out of bounds.")

    def remove_edge(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            from_vertex_node = self.vertices[from_vertex]
            
            if not from_vertex_node.adj_list:
                print(f"No edges from vertex {from_vertex}.")
                return

            current = from_vertex_node.adj_list
            previous = None
            
            # Traverse the circular linked list to find the edge
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

    def get_weight(self, from_vertex, to_vertex):
        if 0 <= from_vertex < self.num_vertices and 0 <= to_vertex < self.num_vertices:
            from_vertex_node = self.vertices[from_vertex]
            current = from_vertex_node.adj_list

            # Traverse the circular linked list to find the weight
            while current:
                if current.vertex == to_vertex:
                    return current.weight
                current = current.next
                if current == from_vertex_node.adj_list:
                    break
            print(f"Edge from {from_vertex} to {to_vertex} not found.")
            return None
        else:
            print("Vertex index out of bounds.")
            return None

    def display_graph(self):
        # Display each vertex and its adjacency list
        for vertex in self.vertices:
            print(f"Vertex {vertex.vertex}:", end=" ")
            if vertex.adj_list:
                current = vertex.adj_list
                while True:
                    print(f"({current.vertex}, {current.weight})", end=" -> ")
                    current = current.next
                    if current == vertex.adj_list:
                        break
                print("Back to start")
            else:
                print("No edges.")

graph = WeightedDirectedGraph(4)

graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 0, 4)
graph.display_graph()


