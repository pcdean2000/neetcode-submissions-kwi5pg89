class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        visit = set()
        heap_next = []
        heapq.heappush(heap_next, (-1.0, start_node))

        while heap_next:
            cur_p, cur_node = heapq.heappop(heap_next)
            if cur_node == end_node:
                return -cur_p
            visit.add(cur_node)
            for nei, nei_p in adj[cur_node]:
                if nei in visit:
                    continue
                heapq.heappush(heap_next, (cur_p * nei_p, nei))
        
        return 0
