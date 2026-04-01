class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq_profits = []
        pq_capitals = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(pq_capitals)
        
        for _ in range(k):
            while pq_capitals and w >= pq_capitals[0][0]:
                c, p = heapq.heappop(pq_capitals)
                heapq.heappush(pq_profits, -p)
            if not pq_profits:
                break
            w -= heapq.heappop(pq_profits)
        
        return w