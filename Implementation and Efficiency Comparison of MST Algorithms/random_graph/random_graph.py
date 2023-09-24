import random
from graph.graph import Graph  # Import the Graph class from the graph module

def generate_dense_graph(num_vertices, density, use_matrix=True):
    graph = Graph(num_vertices)
    max_weight = 100 

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < density:
                weight = random.randint(1, max_weight)
                if use_matrix:
                    graph.add_edge_matrix(i, j, weight)
                else:
                    graph.add_edge_list(i, j, weight)

    return graph

def generate_sparse_graph(num_vertices, sparsity, use_matrix=True):
    graph = Graph(num_vertices)
    max_weight = 100  

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < sparsity:
                weight = random.randint(1, max_weight)
                if use_matrix:
                    graph.add_edge_matrix(i, j, weight)
                else:
                    graph.add_edge_list(i, j, weight)

    return graph
