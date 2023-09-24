class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge_matrix(self, source, destination, weight):
        self.adj_matrix[source][destination] = weight
        self.adj_matrix[destination][source] = weight

    def add_edge_list(self, source, destination, weight):
        self.adj_list[source].append((destination, weight))
        self.adj_list[destination].append((source, weight))