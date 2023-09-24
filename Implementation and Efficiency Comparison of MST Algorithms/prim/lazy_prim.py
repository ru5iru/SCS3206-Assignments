import heapq

class LazyPrim:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        num_vertices = self.graph.num_vertices
        mst = []
        visited = [False] * num_vertices
        pq = []

        
        start_vertex = 0
        visited[start_vertex] = True

        for neighbor, weight in self.graph.adj_list[start_vertex]:
            heapq.heappush(pq, (weight, start_vertex, neighbor))

        while pq:
            weight, source, destination = heapq.heappop(pq)

            if visited[destination]:
                continue

            visited[destination] = True
            mst.append((source, destination, weight))

            for neighbor, weight in self.graph.adj_list[destination]:
                if not visited[neighbor]:
                    heapq.heappush(pq, (weight, destination, neighbor))

        return mst