class DSU:
    def __init__(self, n) -> None:
        self.components = n
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
    
    def find(self, node) -> int:
        parent = self.parent[node]
        if parent != node:
            self.parent[node] = self.find(parent)
        return self.parent[node]

    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        self.components -= 1
        return True

    def get_components(self):
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.get_components()