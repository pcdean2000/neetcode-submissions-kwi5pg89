class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, x):
        par = self.parent[x]
        if par != x:
            self.parent[x] = self.find(par)
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = self.parent[px]
        self.size[px] += self.size[py]
        self.components -= 1
        return True
    
    def get_components(self):
        return self.components

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hashmap_points = {i: point for i, point in enumerate(points)}

        heap_edges = []
        for mp1, mp2 in combinations(hashmap_points.items(), 2):
            i1, p1 = mp1
            i2, p2 = mp2
            x1, y1 = p1
            x2, y2 = p2
            w = abs(x1 - x2) + abs(y1 - y2)
            heapq.heappush(heap_edges, [w, i1, i2])

        uf = UnionFind(len(points))
        total = 0
        while uf.get_components() > 1 and heap_edges:
            w, i1, i2 = heapq.heappop(heap_edges)
            if not uf.union(i1, i2):
                continue
            total += w
        
        return total





