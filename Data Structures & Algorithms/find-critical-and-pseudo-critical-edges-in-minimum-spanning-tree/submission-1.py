class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, u):
        par = self.parent[u]
        if u != par:
            self.parent[u] = self.find(par)
        return self.parent[u]

    def union(self, u, v):
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def get_mst(constraint: List, pseudo = False):
            sorted_edges = sorted([[edge[2], i] for i, edge in enumerate(edges) if i not in constraint])

            mst = set()
            total = 0

            uf = UnionFind(n)
            if pseudo:
                u, v, w = edges[constraint[0]]
                uf.union(u, v)
                mst.add(constraint[0])
                total += w
            
            for w, i in sorted_edges:
                u, v, _ = edges[i]
                if not uf.union(u, v):
                    continue
                mst.add(i)
                total += w
                if uf.get_components() == 1:
                    break
            
            return (total, mst) if uf.get_components() == 1 else (200000, mst)
        
        base_w, mst = get_mst([])

        crit = []
        pseu = []

        for i in range(len(edges)):
            w, mst = get_mst([i])
            if w > base_w:
                crit.append(i)
                continue
            w, mst = get_mst([i], pseudo=True)
            if w == base_w:
                pseu.append(i)
        
        return [crit, pseu]