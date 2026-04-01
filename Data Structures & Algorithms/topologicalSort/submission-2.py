class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, adj, seen, path, topo):
            if node in path:
                return False
            if node in seen:
                return True
            path.add(node)
            if adj[node]:
                for child in adj[node]:
                    if not dfs(child, adj, seen, path, topo):
                        return False
            seen.add(node)
            topo.append(node)
            path.remove(node)
            return True
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        seen = set()
        topo = []
        path = set()
        for node in range(n):
            if node in seen:
                continue
            if not dfs(node, adj, seen, path, topo):
                return []
            print(seen)
            print(topo)
        
        return topo[::-1]