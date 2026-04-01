class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        heap_edges = []
        visit = set()
        heapq.heappush(heap_edges, (0, 0, 0))

        total = 0
        while len(visit) < n and heap_edges:
            w, u, v = heapq.heappop(heap_edges)
            if v in visit:
                continue
            total += w
            visit.add(v)
            for nei, w in adj[v]:
                if nei in visit:
                    continue
                heapq.heappush(heap_edges, (w, v, nei))
        
        return total if len(visit) == n else -1