class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        return root