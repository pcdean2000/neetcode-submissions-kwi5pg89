class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, adj, seen, path, topo):
            if node in path:
                return False
            res = True
            if node in seen:
                return res
            path.append(node)
            if adj[node]:
                for child in adj[node]:
                    res &= dfs(child, adj, seen, path, topo)
            seen.add(node)
            topo.append(node)
            path.pop()
            return res
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        seen = set()
        topo = []
        path = []
        for node in range(n):
            if node in seen:
                continue
            if not dfs(node, adj, seen, path, topo):
                return []
            print(seen)
            print(topo)
        
        return topo[::-1]