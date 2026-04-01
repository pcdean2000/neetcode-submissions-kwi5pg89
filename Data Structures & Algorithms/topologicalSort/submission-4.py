class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, adj, state, topo):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            if adj[node]:
                for child in adj[node]:
                    if not dfs(child, adj, state, topo):
                        return False
            topo.append(node)
            state[node] = 2
            return True
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        topo = []
        # 0: unvisited, 1: visiting, 2: visited
        state = [0 for _ in range(n)]
        for node in range(n):
            if state[node] == 2:
                continue
            if not dfs(node, adj, state, topo):
                return []
        
        return topo[::-1]