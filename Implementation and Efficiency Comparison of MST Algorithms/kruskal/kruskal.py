from graph.disjoint_set import DisjointSet  # Import the DisjointSet class from the disjoint_set module

class Kruskal:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        num_vertices = self.graph.num_vertices
        mst = []
        edges = []

        # Create a list of all edges
        for i in range(num_vertices):
            for j, weight in self.graph.adj_list[i]:
                edges.append((i, j, weight))

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        disjoint_set = DisjointSet(num_vertices)

        for edge in edges:
            source, destination, weight = edge
            if disjoint_set.find(source) != disjoint_set.find(destination):
                mst.append(edge)
                disjoint_set.union(source, destination)

        return mst