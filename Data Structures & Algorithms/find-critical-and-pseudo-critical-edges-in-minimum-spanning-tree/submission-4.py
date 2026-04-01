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
            total = 0
            uf = UnionFind(n)
            
            sorted_edges = []
            for u, v, w, i in edges:
                if i not in constraint:
                    sorted_edges.append([w, i, u, v])
                elif pseudo:
                    uf.union(u, v)
                    total += w
            
            for w, i, u, v in sorted_edges:
                if not uf.union(u, v):
                    continue
                total += w
                if uf.get_components() == 1:
                    break
            
            return total if uf.get_components() == 1 else 200000
        
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        
        base_w = get_mst([])

        crit = []
        pseu = []

        for _, _, _, i in edges:
            w = get_mst([i])
            if w > base_w:
                crit.append(i)
                continue
            w = get_mst([i], pseudo=True)
            if w == base_w:
                pseu.append(i)
        
        return [crit, pseu]