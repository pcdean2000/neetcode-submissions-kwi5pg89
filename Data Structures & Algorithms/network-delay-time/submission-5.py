class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        max_dist = 0
        visit = set()
        heap_delay = []
        heapq.heappush(heap_delay, (0, k))

        while heap_delay and len(visit) < n:
            cur_t, node = heapq.heappop(heap_delay)
            if node in visit:
                continue
            max_dist = cur_t
            for nei, nei_t in adj[node]:
                heapq.heappush(heap_delay, (nei_t + cur_t, nei))
            visit.add(node)
        
        return max_dist if len(visit) == n else -1