class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        
        dijkstra = {i: -1 for i in range(n)}
        visit = set()
        heap_next = []
        heapq.heappush(heap_next, (0, src))

        while heap_next and len(visit) < n:
            w, node = heapq.heappop(heap_next)
            if node in visit:
                continue
            dijkstra[node] = w
            for nei, nei_w in adj[node]:
                heapq.heappush(heap_next, (w + nei_w, nei))
            visit.add(node)

        return dijkstra
