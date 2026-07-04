class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        degree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)
        
        while q:
            u = q.popleft()
            degree[u] -= 1
            for v in adj[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    q.append(v)
        
        for u, v in reversed(edges):
            if degree[u] > 0 and degree[v] > 0:
                return [u, v]
        return []

        
