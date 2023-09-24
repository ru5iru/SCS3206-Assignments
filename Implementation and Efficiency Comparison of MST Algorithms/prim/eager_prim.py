class EagerPrim:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        num_vertices = self.graph.num_vertices
        mst = []
        key = [float('inf')] * num_vertices
        in_mst = [False] * num_vertices

        
        key[0] = 0

        for _ in range(num_vertices):
            u = self._min_key_vertex(key, in_mst)
            in_mst[u] = True

            for v, weight in self.graph.adj_list[u]:
                if not in_mst[v] and weight < key[v]:
                    key[v] = weight

        for v in range(1, num_vertices):
            mst.append((v, v, key[v]))

        return mst

    def _min_key_vertex(self, key, in_mst):
        min_key = float('inf')
        min_vertex = -1

        for v in range(len(key)):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                min_vertex = v

        return min_vertex