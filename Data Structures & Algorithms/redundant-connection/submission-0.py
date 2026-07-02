class UnionSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, u):
        pu = self.parent[u]
        while pu != self.parent[pu]:
            self.parent[pu] = self.parent[self.parent[pu]]
            pu = self.parent[pu]
        return pu

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu

        self.parent[pu] = pv
        self.rank[pv] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        us = UnionSet(len(edges))
        res = []
        for edge in edges:
            if not us.union(edge[0], edge[1]):
                res = edge
        return res